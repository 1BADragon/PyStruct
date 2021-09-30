import struct

from .abstractfield import AbstractField

class BasicField(AbstractField):
    def __init__(self, fmt, **kwargs):
        self._struct = struct.Struct(fmt)
        self._attrs = kwargs

    def __str__(self):
        return f'<PyStruct Field: \"{self._struct.format}\">'

    def _pack(self, val):
        return self._struct.pack(val)

    def _unpack(self, data, offset=0):
        return self._struct.unpack_from(data, offset)[0]

    @property
    def size(self):
        return self._struct.size

    @property
    def default(self):
        return self._attrs.get('default', None)



def field(type_spec):
    if isinstance(type_spec, str):
        return BasicField(type_spec)
    
    raise ValueError(f'{type_spec} cannot be coerced into a field')