from .fieldspec import FieldSpec
from .fields.arrayfield import ArrayField

u8 = '!B'
i8 = '!b'
u16 = '!H'
i16 = '!h'
u32 = '!I'
i32 = '!i'
u64 = '!Q'
i64 = '!q'

class Array(FieldSpec):
    def __init__(self, type_spec, size, **kwargs):
        self._spec = type_spec
        self._size = size
        self._attrs = kwargs

    def build_field(self):
        return ArrayField(self._spec, self._size, **self._attrs)

