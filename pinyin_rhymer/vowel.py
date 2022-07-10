from enum import Enum

VOWEL_TRANSLATION = {
    'i': 'yi',
    'ie': 'ye',
    'ia': 'ya',
    'iu': 'you',
    'iao': 'yao',
    'in': 'yin',
    'ian': 'yan',
    'ing': 'ying',
    'iong': 'yong',
    'iang': 'yang',
    'u': 'wu',
    'o': 'wo',
    'uo': 'wo',
    'ua': 'wa',
    'ui': 'wei',
    'uai': 'wai',
    'uan': 'wan',
    'un': 'wen',
    'uang': 'wang',
    'v': 'yu',
    've': 'yue',
    'vn': 'yun',
    'van': 'yuan'
}


class Monophthong(Enum):
    z = (0, 0.3)
    v = (0.1, 0.2)
    u = (0.1, 0.9)
    i = (0.2, 0.1)
    r = (0.2, 0.7)
    ɚ = (0.4, 0.9)
    e = (0.4, 0.6)
    ɤ = (0.5, 0.8)
    o = (0.6, 0.8)
    a = (0.8, 0.64)

    def __init__(self, openness, backness):
        self.openness = openness
        self.backness = backness

    def similar(self, threshold=0.3):
        return [name for name in self.__class__ if (
            abs(name.backness - self.backness) < 0.3 and
            abs(name.openness - self.openness) < 0.3
        )]


class Vowel(Enum):
    e = ('e', '', 'ɤ', '')
    a = ('a', '', 'a', '')
    ei = ('ei', '', 'e', 'i')
    ai = ('ai', '', 'a', 'i')
    ou = ('ou', '', 'o', 'u')
    ao = ('ao', '', 'a', 'u')
    en = ('en', '', 'e', 'n')
    an = ('an', '', 'a', 'n')
    eng = ('eng', '', 'e', 'ng')
    ang = ('ang', '', 'a', 'ng')
    er = ('er', '', 'ɚ', '')
    yi = ('i', '', 'i', '')
    z = ('i', '', 'z', '')
    r = ('i', '', 'r', '')
    ye = ('ie', 'i', 'e', '')
    ya = ('ia', 'i', 'a', '')
    you = ('iu', 'i', 'o', 'u')
    yao = ('iao', 'i', 'a', 'u')
    yin = ('in', '', 'i', 'n')
    yan = ('ian', 'i', 'a', 'n')
    ying = ('ing', '', 'i', 'ng')
    yong = ('iong', 'i', 'o', 'ng')
    yang = ('iang', 'i', 'a', 'ng')
    wu = ('u', '', 'u', '')
    wo = ('uo', 'u', 'o', '')
    wa = ('ua', 'u', 'a', '')
    wei = ('ui', 'u', 'e', 'i')
    wai = ('uai', 'u', 'a', 'i')
    wen = ('un', 'u', 'e', 'n')
    wan = ('uan', 'u', 'a', 'n')
    weng = ('weng', 'u', 'e', 'ng')
    wang = ('uang', 'u', 'a', 'ng')
    yu = ('v', '', 'v', '')
    yue = ('ve', 'v', 'e', '')
    yun = ('vn', '', 'v', 'n')
    yuan = ('van', 'v', 'a', 'n')

    def __new__(cls, spell, medial, nucleus, coda, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        obj.spell = spell
        obj.medial = medial
        obj.nucleus = nucleus
        obj.coda = coda
        return obj

    @classmethod
    def _missing_(cls, s):
        if s in VOWEL_TRANSLATION:
            s = VOWEL_TRANSLATION[s]
        return Vowel[s]

    @property
    def with_consonant(self):
        return self.spell

    @property
    def without_consonant(self):
        return 'yi' if self.spell == 'i' else self.name

    def similar_traditional(self):
        cls = self.__class__
        return {x for x in cls if (
            x.nucleus == self.nucleus and x.coda == self.coda
        )}
