from .abstractfield import AbstractField

class StringField(AbstractField):
    def __init__(self, size, **kwargs):
        self._size = size
        self._attrs = kwargs

    def _pack(self, val):
        if isinstance(val, str):
            val = val.encode()
        else:
            val = bytes(val)

        if len(val) > self._size:
            raise ValueError(f'String too large for packing')

        return val + b'\x00' * (self._size - len(val))

    def _unpack(self, data, offset=0):
        u = data[offset:offset + self._size]
        offset += self._size
        return u, offset

    @property
    def size(self):
        return self._size

    @property
    def default(self):
        return b'\x00' * self._size