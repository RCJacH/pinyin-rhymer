import re

from pinyin_rhymer.consonant import Consonant
from pinyin_rhymer.vowel import Vowel

TONES = 'āēīōūǖáéíóúǘǎěǐǒǔǚàèìòùǜ'
REPLACE = 'aāáǎàeēéěèiīíǐìoōóǒòuūúǔùvǖǘǚǜ'
ZCS = 'zcs'
ZHCHSHR = ('zh', 'ch', 'sh', 'r')
BPMF = 'bpmf'
JQX = 'jqx'
RE_PINYIN = re.compile(fr'^([{Consonant.all()}]*)([eaiouvngwy]+)(\d)?')


def convert_unicode_to_alnum(pinyin):
    """
    Convert an unicode string of pinyin into an alphanumeric one.
    """
    for c in pinyin:
        if c in TONES:
            i = TONES.find(c)
            vowel = i % 6
            tone = i // 6 + 1
            pinyin = f'{pinyin.replace(c, REPLACE[vowel*5])}{tone}'
            break
    return pinyin


def transform_vowel(consonant, vowel):
    match vowel:
        case 'i':
            if consonant in ZCS:
                return 'z'
            if consonant in ZHCHSHR:
                return 'r'
        case 'o':
            if consonant in BPMF:
                return 'uo'
    if consonant and consonant in JQX:
        return vowel.replace('u', 'v')
    return vowel


class PinYin(object):
    def __init__(self, pinyin):
        if not pinyin.isascii():
            pinyin = convert_unicode_to_alnum(pinyin)
        groups = RE_PINYIN.match(pinyin)
        consonant = groups.group(1)
        vowel = groups.group(2)
        vowel = transform_vowel(consonant, vowel)
        self.consonant = Consonant.get(consonant)
        self.vowel = Vowel(vowel)
        self.tone = int(groups.group(3) or 5)
