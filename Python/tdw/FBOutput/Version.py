# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class Version(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsVersion(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = Version()
        x.Init(buf, n + offset)
        return x

    # Version
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # Version
    def Unity(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Version
    def Tdw(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Version
    def Standalone(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(tdw.flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def VersionStart(builder): builder.StartObject(3)
def VersionAddUnity(builder, unity): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(unity), 0)
def VersionAddTdw(builder, tdw): builder.PrependUOffsetTRelativeSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(tdw), 0)
def VersionAddStandalone(builder, standalone): builder.PrependBoolSlot(2, standalone, 0)
def VersionEnd(builder): return builder.EndObject()
