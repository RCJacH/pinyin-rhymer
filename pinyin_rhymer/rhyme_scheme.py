from enum import Enum, auto


class RhymeScheme(Enum):
    ALL_CONSONANTS = auto()
    FAMILY = auto()
    TRADITIONAL = auto()
    SIMILAR_SOUNDING = auto()
    ADDTIIVE = auto()
    SUBTRACTIVE = auto()

    @classmethod
    def _missing_(cls, name):
        return cls(cls.__members__[name])
