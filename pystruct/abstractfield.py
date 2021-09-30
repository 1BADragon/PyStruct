from abc import ABC

class AbstractField(ABC):
    def _pack(self, val):
        raise NotImplementedError

    def _unpack(self, data, offset=0):
        raise NotImplementedError

    def _visit_setter(self, sruct, name, val):
        raise NotImplementedError

    @property
    def size(self):
        raise NotImplementedError

    @property
    def default(self):
        raise NotImplementedError