from .abstractfield import AbstractField

class StructField(AbstractField):
    def __init__(self, spec, **kwargs):
        self._inner = spec
        self._attrs = kwargs

    def _pack(self, val):
        if not isinstance(val, self._inner):
            raise ValueError(f'Invalid type {type(val)}')

        return val._pack();

    def _unpack(self, data, offset=0):
        tmp = self._inner()

        offset = tmp._unpack(data, offset)
        return (tmp, offset)

    def _visit_setter(self, struct, name, val):
        if type(val) is not self._inner:
            raise ValueError(f"Invalid type {type(val)} for {name}")
        
    @property
    def size(self):
        return self._inner().size

    @property
    def default(self):
        return self._inner()