import struct

from .abstractfield import AbstractField


class BasicField(AbstractField):
    def __init__(self, fmt, **kwargs):
        self._struct = struct.Struct(fmt)
        self._attrs = kwargs

    def __str__(self):
        return f'<PyStruct Field: \"{self._struct.format}\">'

    def _pack(self, val):
        try:
            return self._struct.pack(val)
        except struct.error as e:
            raise ValueError(f"Invalid value \"{val}\" -- {e}")

    def _unpack(self, data, offset=0):
        val = self._struct.unpack_from(data, offset)[0]
        offset += self._struct.size
        return (val, offset)

    @property
    def size(self):
        return self._struct.size

    @property
    def default(self):
        return self._attrs.get('default', None)