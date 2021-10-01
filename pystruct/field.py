from .fields.basicfield import BasicField
from .fieldspec import FieldSpec

def field(type_spec):
    if isinstance(type_spec, str):
        return BasicField(type_spec)
    elif isinstance(type_spec, FieldSpec):
        return type_spec.build_field()
    
    raise ValueError(f'{type_spec} cannot be coerced into a field')