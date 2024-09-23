import asyncio
import multiprocessing.queues as mpq
import queue
from collections.abc import AsyncGenerator, Callable
from concurrent.futures import Future, ThreadPoolExecutor
from contextlib import suppress
from typing import Tuple, Type, TypeVar

T = TypeVar("T")
I = TypeVar("I")
R = TypeVar("R")


async def InterruptableAgen(
    agen: AsyncGenerator[T],
    interrupt: asyncio.Queue[I],
    timeout: float,
) -> AsyncGenerator[T | I]:
    queue: asyncio.Queue[T | StopAsyncIteration] = asyncio.Queue()

    async def producer():
        async for item in agen:
            await queue.put(item)
        await queue.put(StopAsyncIteration())

    producer_task = None
    try:
        producer_task = asyncio.create_task(producer())
        while True:
            with suppress(asyncio.TimeoutError):
                item = await asyncio.wait_for(queue.get(), timeout=timeout)
                # it is not timeout if we reach this line
                if isinstance(item, StopAsyncIteration):
                    break
                else:
                    yield item

            with suppress(asyncio.QueueEmpty):
                v = interrupt.get_nowait()
                # we are interrupted if we reach this line
                yield v
                break

    finally:
        if producer_task:
            producer_task.cancel()
            await producer_task


E = TypeVar("E")


async def ForeverAgen(
    agen_factory: Callable[[], AsyncGenerator[T]], exceptions: Tuple[Type[E]]
) -> AsyncGenerator[T | E]:
    """Run a async generator forever until its cancelled.

    Args:
        agen_factory: a callable that returns the async generator of type T
        exceptions: a tuple of exceptions that should be suppressed and yielded.
            Exceptions not listed here will be re-raised.

    Returns:
        An async generator that yields T or yields the suppressed exceptions.
    """
    while True:
        agen = agen_factory()
        try:
            async for item in agen:
                yield item
        except Exception as e:
            if isinstance(e, exceptions):
                yield e
            else:
                raise


async def QueueAgen(
    inbound: queue.Queue[T] | asyncio.Queue[T] | mpq.Queue[T],
) -> AsyncGenerator[T]:
    if isinstance(inbound, asyncio.Queue):
        while True:
            yield await inbound.get()
            inbound.task_done()
    elif isinstance(inbound, queue.Queue):
        while True:
            yield await asyncio.to_thread(inbound.get)
            inbound.task_done()
    elif isinstance(inbound, mpq.Queue):
        while True:
            yield await asyncio.to_thread(inbound.get)
    else:
        raise TypeError(f"unsupported queue type: {type(inbound)}")


def MapFuture(
    fn: Callable[[T], R], fut: Future[T], pool: ThreadPoolExecutor
) -> Future[R]:
    def task(fn: Callable[[T], R], fut: Future[T]) -> R:
        return fn(fut.result())

    return pool.submit(task, fn, fut)