# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import username_proof_pb2 as username__proof__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x1a\x14username_proof.proto\"\xcc\x01\n\x07Message\x12\x1a\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0c.MessageData\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12 \n\x0bhash_scheme\x18\x03 \x01(\x0e\x32\x0b.HashScheme\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12*\n\x10signature_scheme\x18\x05 \x01(\x0e\x32\x10.SignatureScheme\x12\x0e\n\x06signer\x18\x06 \x01(\x0c\x12\x17\n\ndata_bytes\x18\x07 \x01(\x0cH\x00\x88\x01\x01\x42\r\n\x0b_data_bytes\"\xd5\x04\n\x0bMessageData\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.MessageType\x12\x0b\n\x03\x66id\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\r\x12\"\n\x07network\x18\x04 \x01(\x0e\x32\x11.FarcasterNetwork\x12%\n\rcast_add_body\x18\x05 \x01(\x0b\x32\x0c.CastAddBodyH\x00\x12+\n\x10\x63\x61st_remove_body\x18\x06 \x01(\x0b\x32\x0f.CastRemoveBodyH\x00\x12&\n\rreaction_body\x18\x07 \x01(\x0b\x32\r.ReactionBodyH\x00\x12\x44\n\x1dverification_add_address_body\x18\t \x01(\x0b\x32\x1b.VerificationAddAddressBodyH\x00\x12;\n\x18verification_remove_body\x18\n \x01(\x0b\x32\x17.VerificationRemoveBodyH\x00\x12\'\n\x0euser_data_body\x18\x0c \x01(\x0b\x32\r.UserDataBodyH\x00\x12\x1e\n\tlink_body\x18\x0e \x01(\x0b\x32\t.LinkBodyH\x00\x12-\n\x13username_proof_body\x18\x0f \x01(\x0b\x32\x0e.UserNameProofH\x00\x12-\n\x11\x66rame_action_body\x18\x10 \x01(\x0b\x32\x10.FrameActionBodyH\x00\x12\x38\n\x17link_compact_state_body\x18\x11 \x01(\x0b\x32\x15.LinkCompactStateBodyH\x00\x42\x06\n\x04\x62ody\":\n\x0cUserDataBody\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.UserDataType\x12\r\n\x05value\x18\x02 \x01(\t\";\n\x05\x45mbed\x12\r\n\x03url\x18\x01 \x01(\tH\x00\x12\x1a\n\x07\x63\x61st_id\x18\x02 \x01(\x0b\x32\x07.CastIdH\x00\x42\x07\n\x05\x65mbed\"\xd8\x01\n\x0b\x43\x61stAddBody\x12\x19\n\x11\x65mbeds_deprecated\x18\x01 \x03(\t\x12\x10\n\x08mentions\x18\x02 \x03(\x04\x12!\n\x0eparent_cast_id\x18\x03 \x01(\x0b\x32\x07.CastIdH\x00\x12\x14\n\nparent_url\x18\x07 \x01(\tH\x00\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x1a\n\x12mentions_positions\x18\x05 \x03(\r\x12\x16\n\x06\x65mbeds\x18\x06 \x03(\x0b\x32\x06.Embed\x12\x17\n\x04type\x18\x08 \x01(\x0e\x32\t.CastTypeB\x08\n\x06parent\"%\n\x0e\x43\x61stRemoveBody\x12\x13\n\x0btarget_hash\x18\x01 \x01(\x0c\"#\n\x06\x43\x61stId\x12\x0b\n\x03\x66id\x18\x01 \x01(\x04\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\"n\n\x0cReactionBody\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.ReactionType\x12!\n\x0etarget_cast_id\x18\x02 \x01(\x0b\x32\x07.CastIdH\x00\x12\x14\n\ntarget_url\x18\x03 \x01(\tH\x00\x42\x08\n\x06target\"\xa4\x01\n\x1aVerificationAddAddressBody\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x17\n\x0f\x63laim_signature\x18\x02 \x01(\x0c\x12\x12\n\nblock_hash\x18\x03 \x01(\x0c\x12\x19\n\x11verification_type\x18\x04 \x01(\r\x12\x10\n\x08\x63hain_id\x18\x05 \x01(\r\x12\x1b\n\x08protocol\x18\x07 \x01(\x0e\x32\t.Protocol\"F\n\x16VerificationRemoveBody\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x1b\n\x08protocol\x18\x02 \x01(\x0e\x32\t.Protocol\"l\n\x08LinkBody\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x1d\n\x10\x64isplayTimestamp\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x14\n\ntarget_fid\x18\x03 \x01(\x04H\x00\x42\x08\n\x06targetB\x13\n\x11_displayTimestamp\"9\n\x14LinkCompactStateBody\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0btarget_fids\x18\x02 \x03(\x04\"\x9a\x01\n\x0f\x46rameActionBody\x12\x0b\n\x03url\x18\x01 \x01(\x0c\x12\x14\n\x0c\x62utton_index\x18\x02 \x01(\r\x12\x18\n\x07\x63\x61st_id\x18\x03 \x01(\x0b\x32\x07.CastId\x12\x12\n\ninput_text\x18\x04 \x01(\x0c\x12\r\n\x05state\x18\x05 \x01(\x0c\x12\x16\n\x0etransaction_id\x18\x06 \x01(\x0c\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\x0c*:\n\nHashScheme\x12\x14\n\x10HASH_SCHEME_NONE\x10\x00\x12\x16\n\x12HASH_SCHEME_BLAKE3\x10\x01*g\n\x0fSignatureScheme\x12\x19\n\x15SIGNATURE_SCHEME_NONE\x10\x00\x12\x1c\n\x18SIGNATURE_SCHEME_ED25519\x10\x01\x12\x1b\n\x17SIGNATURE_SCHEME_EIP712\x10\x02*\xb1\x03\n\x0bMessageType\x12\x15\n\x11MESSAGE_TYPE_NONE\x10\x00\x12\x19\n\x15MESSAGE_TYPE_CAST_ADD\x10\x01\x12\x1c\n\x18MESSAGE_TYPE_CAST_REMOVE\x10\x02\x12\x1d\n\x19MESSAGE_TYPE_REACTION_ADD\x10\x03\x12 \n\x1cMESSAGE_TYPE_REACTION_REMOVE\x10\x04\x12\x19\n\x15MESSAGE_TYPE_LINK_ADD\x10\x05\x12\x1c\n\x18MESSAGE_TYPE_LINK_REMOVE\x10\x06\x12-\n)MESSAGE_TYPE_VERIFICATION_ADD_ETH_ADDRESS\x10\x07\x12$\n MESSAGE_TYPE_VERIFICATION_REMOVE\x10\x08\x12\x1e\n\x1aMESSAGE_TYPE_USER_DATA_ADD\x10\x0b\x12\x1f\n\x1bMESSAGE_TYPE_USERNAME_PROOF\x10\x0c\x12\x1d\n\x19MESSAGE_TYPE_FRAME_ACTION\x10\r\x12#\n\x1fMESSAGE_TYPE_LINK_COMPACT_STATE\x10\x0e*\x8a\x01\n\x10\x46\x61rcasterNetwork\x12\x1a\n\x16\x46\x41RCASTER_NETWORK_NONE\x10\x00\x12\x1d\n\x19\x46\x41RCASTER_NETWORK_MAINNET\x10\x01\x12\x1d\n\x19\x46\x41RCASTER_NETWORK_TESTNET\x10\x02\x12\x1c\n\x18\x46\x41RCASTER_NETWORK_DEVNET\x10\x03*\xfc\x01\n\x0cUserDataType\x12\x17\n\x13USER_DATA_TYPE_NONE\x10\x00\x12\x16\n\x12USER_DATA_TYPE_PFP\x10\x01\x12\x1a\n\x16USER_DATA_TYPE_DISPLAY\x10\x02\x12\x16\n\x12USER_DATA_TYPE_BIO\x10\x03\x12\x16\n\x12USER_DATA_TYPE_URL\x10\x05\x12\x1b\n\x17USER_DATA_TYPE_USERNAME\x10\x06\x12\x1b\n\x17USER_DATA_TYPE_LOCATION\x10\x07\x12\x1a\n\x16USER_DATA_TYPE_TWITTER\x10\x08\x12\x19\n\x15USER_DATA_TYPE_GITHUB\x10\t*#\n\x08\x43\x61stType\x12\x08\n\x04\x43\x41ST\x10\x00\x12\r\n\tLONG_CAST\x10\x01*X\n\x0cReactionType\x12\x16\n\x12REACTION_TYPE_NONE\x10\x00\x12\x16\n\x12REACTION_TYPE_LIKE\x10\x01\x12\x18\n\x14REACTION_TYPE_RECAST\x10\x02*6\n\x08Protocol\x12\x15\n\x11PROTOCOL_ETHEREUM\x10\x00\x12\x13\n\x0fPROTOCOL_SOLANA\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HASHSCHEME._serialized_start=1939
  _HASHSCHEME._serialized_end=1997
  _SIGNATURESCHEME._serialized_start=1999
  _SIGNATURESCHEME._serialized_end=2102
  _MESSAGETYPE._serialized_start=2105
  _MESSAGETYPE._serialized_end=2538
  _FARCASTERNETWORK._serialized_start=2541
  _FARCASTERNETWORK._serialized_end=2679
  _USERDATATYPE._serialized_start=2682
  _USERDATATYPE._serialized_end=2934
  _CASTTYPE._serialized_start=2936
  _CASTTYPE._serialized_end=2971
  _REACTIONTYPE._serialized_start=2973
  _REACTIONTYPE._serialized_end=3061
  _PROTOCOL._serialized_start=3063
  _PROTOCOL._serialized_end=3117
  _MESSAGE._serialized_start=40
  _MESSAGE._serialized_end=244
  _MESSAGEDATA._serialized_start=247
  _MESSAGEDATA._serialized_end=844
  _USERDATABODY._serialized_start=846
  _USERDATABODY._serialized_end=904
  _EMBED._serialized_start=906
  _EMBED._serialized_end=965
  _CASTADDBODY._serialized_start=968
  _CASTADDBODY._serialized_end=1184
  _CASTREMOVEBODY._serialized_start=1186
  _CASTREMOVEBODY._serialized_end=1223
  _CASTID._serialized_start=1225
  _CASTID._serialized_end=1260
  _REACTIONBODY._serialized_start=1262
  _REACTIONBODY._serialized_end=1372
  _VERIFICATIONADDADDRESSBODY._serialized_start=1375
  _VERIFICATIONADDADDRESSBODY._serialized_end=1539
  _VERIFICATIONREMOVEBODY._serialized_start=1541
  _VERIFICATIONREMOVEBODY._serialized_end=1611
  _LINKBODY._serialized_start=1613
  _LINKBODY._serialized_end=1721
  _LINKCOMPACTSTATEBODY._serialized_start=1723
  _LINKCOMPACTSTATEBODY._serialized_end=1780
  _FRAMEACTIONBODY._serialized_start=1783
  _FRAMEACTIONBODY._serialized_end=1937
# @@protoc_insertion_point(module_scope)
