from enum import Enum, auto

from pinyin_rhymer.error import NotARhymeSchemeError


class SchemeMethods(Enum):
    @classmethod
    def _missing_(cls, name):
        if isinstance(name, cls):
            return name
        try:
            name = cls.__members__[name]
        except KeyError:
            raise NotARhymeSchemeError(name, cls)
        return cls(name)


class ConsonantScheme(SchemeMethods):
    ALL = auto()
    FAMILY = auto()


class VowelScheme(SchemeMethods):
    TRADITIONAL = auto()
    FOURTEEN_RHYMES = auto()
    SIMILAR_SOUNDING = auto()
    ADDTIIVE = auto()
    SUBTRACTIVE = auto()
