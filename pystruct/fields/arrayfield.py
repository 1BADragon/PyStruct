from .abstractfield import AbstractField
from ..field import field

class ArrayField(AbstractField):
    def __init__(self, fmt, size, **kwargs):
        self._inner = field(fmt)
        self._size = size
        self._attrs = kwargs

    def _pack(self, val):
        if not isinstance(val, list) or len(val) != self._size:
            raise ValueError("Invalid list size")
        
        packed = bytes()
        for v in val:
            packed += self._inner._pack(v)

        return bytes(packed)

    def _unpack(self, data, offset=0):
        l = list()
        for _ in range(self._size):
            val, offset = self._inner._unpack(data, offset)
            l.append(val)
        return l, offset

    def _visit_setter(self, sruct, name, val):
        raise NotImplementedError

    @property
    def size(self):
        return self._inside.size * self._size

    @property
    def default(self):
        return [self._attrs.get('default', None)] * self._size
