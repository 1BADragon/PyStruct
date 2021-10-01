import collections

from .fields.abstractfield import AbstractField

class PyStructClassMembers(type):
    @classmethod
    def __prepare__(metacls, __name, __bases):
        return collections.OrderedDict()

    def __new__(self, name, bases, classdict):
        classdict['__ordered__'] = [key for key in classdict.keys()
                if key not in ('__module__', '__qualname__')]

        slots = list()
        fields = collections.OrderedDict()

        for k, v in classdict.items():
            if isinstance(v, AbstractField):
                slots.append(k)
                fields[k] = v

        for name in slots:
            del classdict[name]

        classdict['__slots__'] = slots
        classdict['_fields'] = fields

        return type.__new__(self, name, bases, classdict)