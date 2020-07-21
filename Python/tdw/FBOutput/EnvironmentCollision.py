# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class EnvironmentCollision(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEnvironmentCollision(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = EnvironmentCollision()
        x.Init(buf, n + offset)
        return x

    # EnvironmentCollision
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # EnvironmentCollision
    def ObjectId(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EnvironmentCollision
    def State(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(tdw.flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 1

    # EnvironmentCollision
    def Contacts(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j) * 24
            from .ContactPoint import ContactPoint
            obj = ContactPoint()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # EnvironmentCollision
    def ContactsLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def EnvironmentCollisionStart(builder): builder.StartObject(3)
def EnvironmentCollisionAddObjectId(builder, objectId): builder.PrependInt32Slot(0, objectId, 0)
def EnvironmentCollisionAddState(builder, state): builder.PrependUint8Slot(1, state, 1)
def EnvironmentCollisionAddContacts(builder, contacts): builder.PrependUOffsetTRelativeSlot(2, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(contacts), 0)
def EnvironmentCollisionStartContactsVector(builder, numElems): return builder.StartVector(24, numElems, 4)
def EnvironmentCollisionEnd(builder): return builder.EndObject()
