# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class Color(object):
    __slots__ = ['_tab']

    # Color
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # Color
    def R(self): return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Color
    def G(self): return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # Color
    def B(self): return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, self._tab.Pos + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(8))

def CreateColor(builder, r, g, b):
    builder.Prep(4, 12)
    builder.PrependInt32(b)
    builder.PrependInt32(g)
    builder.PrependInt32(r)
    return builder.Offset()