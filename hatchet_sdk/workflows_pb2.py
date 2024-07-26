# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: workflows.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fworkflows.proto\x1a\x1fgoogle/protobuf/timestamp.proto\">\n\x12PutWorkflowRequest\x12(\n\x04opts\x18\x01 \x01(\x0b\x32\x1a.CreateWorkflowVersionOpts\"\xe0\x03\n\x19\x43reateWorkflowVersionOpts\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x16\n\x0e\x65vent_triggers\x18\x04 \x03(\t\x12\x15\n\rcron_triggers\x18\x05 \x03(\t\x12\x36\n\x12scheduled_triggers\x18\x06 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x04jobs\x18\x07 \x03(\x0b\x32\x16.CreateWorkflowJobOpts\x12-\n\x0b\x63oncurrency\x18\x08 \x01(\x0b\x32\x18.WorkflowConcurrencyOpts\x12\x1d\n\x10schedule_timeout\x18\t \x01(\tH\x00\x88\x01\x01\x12\x17\n\ncron_input\x18\n \x01(\tH\x01\x88\x01\x01\x12\x33\n\x0eon_failure_job\x18\x0b \x01(\x0b\x32\x16.CreateWorkflowJobOptsH\x02\x88\x01\x01\x12$\n\x06sticky\x18\x0c \x01(\x0e\x32\x0f.StickyStrategyH\x03\x88\x01\x01\x42\x13\n\x11_schedule_timeoutB\r\n\x0b_cron_inputB\x11\n\x0f_on_failure_jobB\t\n\x07_sticky\"n\n\x17WorkflowConcurrencyOpts\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x10\n\x08max_runs\x18\x02 \x01(\x05\x12\x31\n\x0elimit_strategy\x18\x03 \x01(\x0e\x32\x19.ConcurrencyLimitStrategy\"h\n\x15\x43reateWorkflowJobOpts\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12&\n\x05steps\x18\x04 \x03(\x0b\x32\x17.CreateWorkflowStepOptsJ\x04\x08\x03\x10\x04\"\xe1\x01\n\x13\x44\x65siredWorkerLabels\x12\x15\n\x08strValue\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08intValue\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08required\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12/\n\ncomparator\x18\x04 \x01(\x0e\x32\x16.WorkerLabelComparatorH\x03\x88\x01\x01\x12\x13\n\x06weight\x18\x05 \x01(\x05H\x04\x88\x01\x01\x42\x0b\n\t_strValueB\x0b\n\t_intValueB\x0b\n\t_requiredB\r\n\x0b_comparatorB\t\n\x07_weight\"\xcb\x02\n\x16\x43reateWorkflowStepOpts\x12\x13\n\x0breadable_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\t\x12\x0e\n\x06inputs\x18\x04 \x01(\t\x12\x0f\n\x07parents\x18\x05 \x03(\t\x12\x11\n\tuser_data\x18\x06 \x01(\t\x12\x0f\n\x07retries\x18\x07 \x01(\x05\x12)\n\x0brate_limits\x18\x08 \x03(\x0b\x32\x14.CreateStepRateLimit\x12@\n\rworker_labels\x18\t \x03(\x0b\x32).CreateWorkflowStepOpts.WorkerLabelsEntry\x1aI\n\x11WorkerLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.DesiredWorkerLabels:\x02\x38\x01\"1\n\x13\x43reateStepRateLimit\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05units\x18\x02 \x01(\x05\"\x16\n\x14ListWorkflowsRequest\"\x93\x02\n\x17ScheduleWorkflowRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\tschedules\x18\x02 \x03(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05input\x18\x03 \x01(\t\x12\x16\n\tparent_id\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1f\n\x12parent_step_run_id\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x63hild_index\x18\x06 \x01(\x05H\x02\x88\x01\x01\x12\x16\n\tchild_key\x18\x07 \x01(\tH\x03\x88\x01\x01\x42\x0c\n\n_parent_idB\x15\n\x13_parent_step_run_idB\x0e\n\x0c_child_indexB\x0c\n\n_child_key\"\xb2\x01\n\x0fWorkflowVersion\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\r\n\x05order\x18\x06 \x01(\x05\x12\x13\n\x0bworkflow_id\x18\x07 \x01(\t\"?\n\x17WorkflowTriggerEventRef\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12\x11\n\tevent_key\x18\x02 \x01(\t\"9\n\x16WorkflowTriggerCronRef\x12\x11\n\tparent_id\x18\x01 \x01(\t\x12\x0c\n\x04\x63ron\x18\x02 \x01(\t\"\xd3\x02\n\x16TriggerWorkflowRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05input\x18\x02 \x01(\t\x12\x16\n\tparent_id\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x1f\n\x12parent_step_run_id\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x63hild_index\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x16\n\tchild_key\x18\x06 \x01(\tH\x03\x88\x01\x01\x12 \n\x13\x61\x64\x64itional_metadata\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x1e\n\x11\x64\x65sired_worker_id\x18\x08 \x01(\tH\x05\x88\x01\x01\x42\x0c\n\n_parent_idB\x15\n\x13_parent_step_run_idB\x0e\n\x0c_child_indexB\x0c\n\n_child_keyB\x16\n\x14_additional_metadataB\x14\n\x12_desired_worker_id\"2\n\x17TriggerWorkflowResponse\x12\x17\n\x0fworkflow_run_id\x18\x01 \x01(\t\"W\n\x13PutRateLimitRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\x12$\n\x08\x64uration\x18\x03 \x01(\x0e\x32\x12.RateLimitDuration\"\x16\n\x14PutRateLimitResponse*$\n\x0eStickyStrategy\x12\x08\n\x04SOFT\x10\x00\x12\x08\n\x04HARD\x10\x01*l\n\x18\x43oncurrencyLimitStrategy\x12\x16\n\x12\x43\x41NCEL_IN_PROGRESS\x10\x00\x12\x0f\n\x0b\x44ROP_NEWEST\x10\x01\x12\x10\n\x0cQUEUE_NEWEST\x10\x02\x12\x15\n\x11GROUP_ROUND_ROBIN\x10\x03*\x85\x01\n\x15WorkerLabelComparator\x12\t\n\x05\x45QUAL\x10\x00\x12\r\n\tNOT_EQUAL\x10\x01\x12\x10\n\x0cGREATER_THAN\x10\x02\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x03\x12\r\n\tLESS_THAN\x10\x04\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x05*]\n\x11RateLimitDuration\x12\n\n\x06SECOND\x10\x00\x12\n\n\x06MINUTE\x10\x01\x12\x08\n\x04HOUR\x10\x02\x12\x07\n\x03\x44\x41Y\x10\x03\x12\x08\n\x04WEEK\x10\x04\x12\t\n\x05MONTH\x10\x05\x12\x08\n\x04YEAR\x10\x06\x32\x8a\x02\n\x0fWorkflowService\x12\x34\n\x0bPutWorkflow\x12\x13.PutWorkflowRequest\x1a\x10.WorkflowVersion\x12>\n\x10ScheduleWorkflow\x12\x18.ScheduleWorkflowRequest\x1a\x10.WorkflowVersion\x12\x44\n\x0fTriggerWorkflow\x12\x17.TriggerWorkflowRequest\x1a\x18.TriggerWorkflowResponse\x12;\n\x0cPutRateLimit\x12\x14.PutRateLimitRequest\x1a\x15.PutRateLimitResponseBBZ@github.com/hatchet-dev/hatchet/internal/services/admin/contractsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'workflows_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z@github.com/hatchet-dev/hatchet/internal/services/admin/contracts'
  _globals['_CREATEWORKFLOWSTEPOPTS_WORKERLABELSENTRY']._options = None
  _globals['_CREATEWORKFLOWSTEPOPTS_WORKERLABELSENTRY']._serialized_options = b'8\001'
  _globals['_STICKYSTRATEGY']._serialized_start=2544
  _globals['_STICKYSTRATEGY']._serialized_end=2580
  _globals['_CONCURRENCYLIMITSTRATEGY']._serialized_start=2582
  _globals['_CONCURRENCYLIMITSTRATEGY']._serialized_end=2690
  _globals['_WORKERLABELCOMPARATOR']._serialized_start=2693
  _globals['_WORKERLABELCOMPARATOR']._serialized_end=2826
  _globals['_RATELIMITDURATION']._serialized_start=2828
  _globals['_RATELIMITDURATION']._serialized_end=2921
  _globals['_PUTWORKFLOWREQUEST']._serialized_start=52
  _globals['_PUTWORKFLOWREQUEST']._serialized_end=114
  _globals['_CREATEWORKFLOWVERSIONOPTS']._serialized_start=117
  _globals['_CREATEWORKFLOWVERSIONOPTS']._serialized_end=597
  _globals['_WORKFLOWCONCURRENCYOPTS']._serialized_start=599
  _globals['_WORKFLOWCONCURRENCYOPTS']._serialized_end=709
  _globals['_CREATEWORKFLOWJOBOPTS']._serialized_start=711
  _globals['_CREATEWORKFLOWJOBOPTS']._serialized_end=815
  _globals['_DESIREDWORKERLABELS']._serialized_start=818
  _globals['_DESIREDWORKERLABELS']._serialized_end=1043
  _globals['_CREATEWORKFLOWSTEPOPTS']._serialized_start=1046
  _globals['_CREATEWORKFLOWSTEPOPTS']._serialized_end=1377
  _globals['_CREATEWORKFLOWSTEPOPTS_WORKERLABELSENTRY']._serialized_start=1304
  _globals['_CREATEWORKFLOWSTEPOPTS_WORKERLABELSENTRY']._serialized_end=1377
  _globals['_CREATESTEPRATELIMIT']._serialized_start=1379
  _globals['_CREATESTEPRATELIMIT']._serialized_end=1428
  _globals['_LISTWORKFLOWSREQUEST']._serialized_start=1430
  _globals['_LISTWORKFLOWSREQUEST']._serialized_end=1452
  _globals['_SCHEDULEWORKFLOWREQUEST']._serialized_start=1455
  _globals['_SCHEDULEWORKFLOWREQUEST']._serialized_end=1730
  _globals['_WORKFLOWVERSION']._serialized_start=1733
  _globals['_WORKFLOWVERSION']._serialized_end=1911
  _globals['_WORKFLOWTRIGGEREVENTREF']._serialized_start=1913
  _globals['_WORKFLOWTRIGGEREVENTREF']._serialized_end=1976
  _globals['_WORKFLOWTRIGGERCRONREF']._serialized_start=1978
  _globals['_WORKFLOWTRIGGERCRONREF']._serialized_end=2035
  _globals['_TRIGGERWORKFLOWREQUEST']._serialized_start=2038
  _globals['_TRIGGERWORKFLOWREQUEST']._serialized_end=2377
  _globals['_TRIGGERWORKFLOWRESPONSE']._serialized_start=2379
  _globals['_TRIGGERWORKFLOWRESPONSE']._serialized_end=2429
  _globals['_PUTRATELIMITREQUEST']._serialized_start=2431
  _globals['_PUTRATELIMITREQUEST']._serialized_end=2518
  _globals['_PUTRATELIMITRESPONSE']._serialized_start=2520
  _globals['_PUTRATELIMITRESPONSE']._serialized_end=2542
  _globals['_WORKFLOWSERVICE']._serialized_start=2924
  _globals['_WORKFLOWSERVICE']._serialized_end=3190
# @@protoc_insertion_point(module_scope)
