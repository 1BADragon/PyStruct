import collections

from .pystructclassmembers import PyStructClassMembers

class PyStruct(metaclass=PyStructClassMembers):
    
    def __init__(self):
        for name in self.__slots__:
            setattr(self, name, self._fields[name].default)

    def _pack(self):
        pass

    def _unpack(self, data):
        pass

    # def __getattribute__(self, name):
    #     try:
    #         if name in super(PyStruct, self).__getattribute__('_fields'):
    #             return super(PyStruct, self).__getattribute__('_vals')[name]
    #     except AttributeError:
    #         pass

    #     return super(PyStruct, self).__getattribute__(name)

    # def __setattr__(self, name, value) -> None:
    #     try:
    #         if name in self._fields:
    #             self._vals[name] = value
    #             return
    #     except AttributeError:
    #         pass

    #     super(PyStruct, self).__setattr__(name, value)
    