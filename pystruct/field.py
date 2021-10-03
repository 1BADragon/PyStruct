from .fields.basicfield import BasicField
from .fields.structfield import StructField
from .fieldspec import FieldSpec
from .pystruct import PyStruct

def field(type_spec, **kwargs):
    if isinstance(type_spec, str):
        return BasicField(type_spec, **kwargs)
    elif isinstance(type_spec, FieldSpec):
        return type_spec.build_field(**kwargs)
    elif issubclass(type_spec, PyStruct):
        return StructField(type_spec, **kwargs)
    
    raise ValueError(f'{type_spec} cannot be coerced into a field')