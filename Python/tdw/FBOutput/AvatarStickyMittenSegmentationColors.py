# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class AvatarStickyMittenSegmentationColors(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAvatarStickyMittenSegmentationColors(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = AvatarStickyMittenSegmentationColors()
        x.Init(buf, n + offset)
        return x

    # AvatarStickyMittenSegmentationColors
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # AvatarStickyMittenSegmentationColors
    def Id(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AvatarStickyMittenSegmentationColors
    def BodyParts(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .SegmentationColorData import SegmentationColorData
            obj = SegmentationColorData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AvatarStickyMittenSegmentationColors
    def BodyPartsLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def AvatarStickyMittenSegmentationColorsStart(builder): builder.StartObject(2)
def AvatarStickyMittenSegmentationColorsAddId(builder, id): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def AvatarStickyMittenSegmentationColorsAddBodyParts(builder, bodyParts): builder.PrependUOffsetTRelativeSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(bodyParts), 0)
def AvatarStickyMittenSegmentationColorsStartBodyPartsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def AvatarStickyMittenSegmentationColorsEnd(builder): return builder.EndObject()
