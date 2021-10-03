from abc import ABC

class FieldSpec(ABC):
    def build_field(self, **kwargs):
        raise NotImplementedError