# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LegoControl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Messages_pb2 as Messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11LegoControl.proto\x12\x07\x63ontrol\x1a\x0eMessages.proto\"0\n\x0cImagePreview\x12\r\n\x05image\x18\x01 \x01(\x0c\x12\x11\n\ttimestamp\x18\x02 \x01(\t2G\n\x0bLegoControl\x12\x38\n\x10GetCameraPreview\x12\r.common.Empty\x1a\x15.control.ImagePreviewB\'\n\x13\x63om.lsorter.controlB\x10LegoControlProtob\x06proto3')



_IMAGEPREVIEW = DESCRIPTOR.message_types_by_name['ImagePreview']
ImagePreview = _reflection.GeneratedProtocolMessageType('ImagePreview', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEPREVIEW,
  '__module__' : 'LegoControl_pb2'
  # @@protoc_insertion_point(class_scope:control.ImagePreview)
  })
_sym_db.RegisterMessage(ImagePreview)

_LEGOCONTROL = DESCRIPTOR.services_by_name['LegoControl']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.lsorter.controlB\020LegoControlProto'
  _IMAGEPREVIEW._serialized_start=46
  _IMAGEPREVIEW._serialized_end=94
  _LEGOCONTROL._serialized_start=96
  _LEGOCONTROL._serialized_end=167
# @@protoc_insertion_point(module_scope)
