from abc import ABC

class FieldSpec(ABC):
    def build_field(self):
        raise NotImplementedError