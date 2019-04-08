# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VtsFuzzTaskMessage.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import ComponentSpecificationMessage_pb2
import VtsReportMessage_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='VtsFuzzTaskMessage.proto',
  package='android.vts',
  serialized_pb='\n\x18VtsFuzzTaskMessage.proto\x12\x0b\x61ndroid.vts\x1a#ComponentSpecificationMessage.proto\x1a\x16VtsReportMessage.proto\"\x84\x01\n\x1dTestSuiteSpecificationMessage\x12\x12\n\ntest_suite\x18\x01 \x01(\x0c\x12\x0e\n\x06\x62ranch\x18\x0b \x01(\x0c\x12\x16\n\x0etarget_product\x18\x0c \x01(\x0c\x12\x15\n\rbuild_variant\x18\r \x01(\x0c\x12\x10\n\x08\x62uild_id\x18\x15 \x01(\x0c\"\xf4\x01\n\x1a\x43orpusSpecificationMessage\x12\x34\n\x0f\x63omponent_class\x18\x01 \x01(\x0e\x32\x1b.android.vts.ComponentClass\x12\x18\n\x10\x63orpus_file_name\x18\x02 \x03(\x0c\x12\x18\n\x10hal_package_name\x18\x0b \x01(\x0c\x12\x1a\n\x12hal_transport_type\x18\x0c \x01(\x0c\x12\x19\n\x11hal_major_version\x18\r \x01(\x05\x12\x19\n\x11hal_minor_version\x18\x0e \x01(\x05\x12\x1a\n\x12hal_interface_name\x18\x0f \x01(\x0c\"\x85\x03\n\x13\x46uzzTaskUnitMessage\x12#\n\x06status\x18\x01 \x01(\x0e\x32\x13.android.vts.Status\x12(\n\x0bresult_type\x18\x02 \x01(\x0e\x32\x13.android.vts.Result\x12,\n\x03log\x18\x03 \x03(\x0b\x32\x1f.android.vts.UrlResourceMessage\x12\x1a\n\x12\x63reation_timestamp\x18\x0b \x01(\x03\x12\x1f\n\x17status_change_timestamp\x18\x0c \x01(\x03\x12:\n\x0b\x64\x65vice_info\x18\x15 \x01(\x0b\x32%.android.vts.AndroidDeviceInfoMessage\x12\x31\n\nbuild_info\x18\x16 \x01(\x0b\x32\x1d.android.vts.AndroidBuildInfo\x12\x45\n\x11test_suite_target\x18\x17 \x01(\x0b\x32*.android.vts.TestSuiteSpecificationMessage\"\xad\x01\n\x12VtsFuzzTaskMessage\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x33\n\ttask_unit\x18\x02 \x03(\x0b\x32 .android.vts.FuzzTaskUnitMessage\x12\x18\n\x10test_module_name\x18\x0b \x01(\x0c\x12\x37\n\x06\x63orpus\x18\x15 \x01(\x0b\x32\'.android.vts.CorpusSpecificationMessage*.\n\x06Status\x12\t\n\x05READY\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\r\n\tPROCESSED\x10\x02*I\n\x06Result\x12\x11\n\rNOT_PROCESSED\x10\x00\x12\x13\n\x0f\x43RASH_DUPLICATE\x10\x01\x12\r\n\tCRASH_NEW\x10\x02\x12\x08\n\x04PASS\x10\x03\x42\x30\n\x15\x63om.android.vts.protoB\x17VtsFuzzTaskMessageClass')

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='android.vts.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCKED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESSED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1052,
  serialized_end=1098,
)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='android.vts.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_PROCESSED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRASH_DUPLICATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRASH_NEW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1100,
  serialized_end=1173,
)

Result = enum_type_wrapper.EnumTypeWrapper(_RESULT)
READY = 0
LOCKED = 1
PROCESSED = 2
NOT_PROCESSED = 0
CRASH_DUPLICATE = 1
CRASH_NEW = 2
PASS = 3



_TESTSUITESPECIFICATIONMESSAGE = _descriptor.Descriptor(
  name='TestSuiteSpecificationMessage',
  full_name='android.vts.TestSuiteSpecificationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='test_suite', full_name='android.vts.TestSuiteSpecificationMessage.test_suite', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='branch', full_name='android.vts.TestSuiteSpecificationMessage.branch', index=1,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_product', full_name='android.vts.TestSuiteSpecificationMessage.target_product', index=2,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_variant', full_name='android.vts.TestSuiteSpecificationMessage.build_variant', index=3,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_id', full_name='android.vts.TestSuiteSpecificationMessage.build_id', index=4,
      number=21, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=103,
  serialized_end=235,
)


_CORPUSSPECIFICATIONMESSAGE = _descriptor.Descriptor(
  name='CorpusSpecificationMessage',
  full_name='android.vts.CorpusSpecificationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='component_class', full_name='android.vts.CorpusSpecificationMessage.component_class', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='corpus_file_name', full_name='android.vts.CorpusSpecificationMessage.corpus_file_name', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hal_package_name', full_name='android.vts.CorpusSpecificationMessage.hal_package_name', index=2,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hal_transport_type', full_name='android.vts.CorpusSpecificationMessage.hal_transport_type', index=3,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hal_major_version', full_name='android.vts.CorpusSpecificationMessage.hal_major_version', index=4,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hal_minor_version', full_name='android.vts.CorpusSpecificationMessage.hal_minor_version', index=5,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hal_interface_name', full_name='android.vts.CorpusSpecificationMessage.hal_interface_name', index=6,
      number=15, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=238,
  serialized_end=482,
)


_FUZZTASKUNITMESSAGE = _descriptor.Descriptor(
  name='FuzzTaskUnitMessage',
  full_name='android.vts.FuzzTaskUnitMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='android.vts.FuzzTaskUnitMessage.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_type', full_name='android.vts.FuzzTaskUnitMessage.result_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log', full_name='android.vts.FuzzTaskUnitMessage.log', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_timestamp', full_name='android.vts.FuzzTaskUnitMessage.creation_timestamp', index=3,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_change_timestamp', full_name='android.vts.FuzzTaskUnitMessage.status_change_timestamp', index=4,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_info', full_name='android.vts.FuzzTaskUnitMessage.device_info', index=5,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_info', full_name='android.vts.FuzzTaskUnitMessage.build_info', index=6,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_suite_target', full_name='android.vts.FuzzTaskUnitMessage.test_suite_target', index=7,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=485,
  serialized_end=874,
)


_VTSFUZZTASKMESSAGE = _descriptor.Descriptor(
  name='VtsFuzzTaskMessage',
  full_name='android.vts.VtsFuzzTaskMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='android.vts.VtsFuzzTaskMessage.task_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_unit', full_name='android.vts.VtsFuzzTaskMessage.task_unit', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_module_name', full_name='android.vts.VtsFuzzTaskMessage.test_module_name', index=2,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='corpus', full_name='android.vts.VtsFuzzTaskMessage.corpus', index=3,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=877,
  serialized_end=1050,
)

_CORPUSSPECIFICATIONMESSAGE.fields_by_name['component_class'].enum_type = ComponentSpecificationMessage_pb2._COMPONENTCLASS
_FUZZTASKUNITMESSAGE.fields_by_name['status'].enum_type = _STATUS
_FUZZTASKUNITMESSAGE.fields_by_name['result_type'].enum_type = _RESULT
_FUZZTASKUNITMESSAGE.fields_by_name['log'].message_type = VtsReportMessage_pb2._URLRESOURCEMESSAGE
_FUZZTASKUNITMESSAGE.fields_by_name['device_info'].message_type = VtsReportMessage_pb2._ANDROIDDEVICEINFOMESSAGE
_FUZZTASKUNITMESSAGE.fields_by_name['build_info'].message_type = VtsReportMessage_pb2._ANDROIDBUILDINFO
_FUZZTASKUNITMESSAGE.fields_by_name['test_suite_target'].message_type = _TESTSUITESPECIFICATIONMESSAGE
_VTSFUZZTASKMESSAGE.fields_by_name['task_unit'].message_type = _FUZZTASKUNITMESSAGE
_VTSFUZZTASKMESSAGE.fields_by_name['corpus'].message_type = _CORPUSSPECIFICATIONMESSAGE
DESCRIPTOR.message_types_by_name['TestSuiteSpecificationMessage'] = _TESTSUITESPECIFICATIONMESSAGE
DESCRIPTOR.message_types_by_name['CorpusSpecificationMessage'] = _CORPUSSPECIFICATIONMESSAGE
DESCRIPTOR.message_types_by_name['FuzzTaskUnitMessage'] = _FUZZTASKUNITMESSAGE
DESCRIPTOR.message_types_by_name['VtsFuzzTaskMessage'] = _VTSFUZZTASKMESSAGE

class TestSuiteSpecificationMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTSUITESPECIFICATIONMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.TestSuiteSpecificationMessage)

class CorpusSpecificationMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CORPUSSPECIFICATIONMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.CorpusSpecificationMessage)

class FuzzTaskUnitMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUZZTASKUNITMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.FuzzTaskUnitMessage)

class VtsFuzzTaskMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VTSFUZZTASKMESSAGE

  # @@protoc_insertion_point(class_scope:android.vts.VtsFuzzTaskMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\025com.android.vts.protoB\027VtsFuzzTaskMessageClass')
# @@protoc_insertion_point(module_scope)
