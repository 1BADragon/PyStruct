import collections

from .pystructclassmembers import PyStructClassMembers

class PyStruct(metaclass=PyStructClassMembers):
    
    def __init__(self):
        for name in self.__slots__:
            setattr(self, name, self._fields[name].default)

    def _pack(self):
        data = bytearray()

        for s in self.__slots__:
            if s is None:
                raise ValueError("Field {name} not set")
            data += self._fields[s]._pack(getattr(self, s))

        return bytes(data)

    def _unpack(self, data, offset=0):
        for name, f in self._fields.items():
            val, offset = f._unpack(data, offset)
            setattr(self, name, val)

        return offset
         
    