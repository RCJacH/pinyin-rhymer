from enum import Enum

import pytest

from pinyin_rhymer.consonant import Consonant
from pinyin_rhymer.pinyin import PinYin


class PinyinCase(Enum):
    a5 = ('a', '', 'a', 'a', '', 'a', '', 5)
    bo3 = ('bǒ', 'b', 'wo', 'uo', 'u', 'o', '', 3)
    pu1 = ('pū', 'p', 'wu', 'u', '', 'u', '', 1)
    ming3 = ('mǐng', 'm', 'ying', 'ing', '', 'i', 'ng', 3)
    fen2 = ('fén', 'f', 'en', 'en', '', 'e', 'n', 2)
    dai4 = ('dài', 'd', 'ai', 'ai', '', 'a', 'i', 4)
    tu1 = ('tū', 't', 'wu', 'u', '', 'u', '', 1)
    nv3 = ('nǚ', 'n', 'yu', 'v', '', 'v', '', 3)
    liu2 = ('líu', 'l', 'you', 'iu', 'i', 'o', 'u', 2)
    gang4 = ('gàng', 'g', 'ang', 'ang', '', 'a', 'ng', 4)
    ke3 = ('kě', 'k', 'e', 'e', '', 'ɤ', '', 3)
    hui2 = ('húi', 'h', 'wei', 'ui', 'u', 'e', 'i', 2)
    jue1 = ('jūe', 'j', 'yue', 've', 'v', 'e', '', 1)
    qu4 = ('qù', 'q', 'yu', 'v', '', 'v', '', 4)
    xie2 = ('xié', 'x', 'ye', 'ie', 'i', 'e', '', 2)
    zhao1 = ('zhāo', 'zh', 'ao', 'ao', '', 'a', 'u', 1)
    chuang1 = ('chuāng', 'ch', 'wang', 'uang', 'u', 'a', 'ng', 1)
    shi4 = ('shì', 'sh', 'r', 'i', '', 'r', '', 4)
    rou3 = ('rǒu', 'r', 'ou', 'ou', '', 'o', 'u', 3)
    zan4 = ('zàn', 'z', 'an', 'an', '', 'a', 'n', 4)
    ci2 = ('cí', 'c', 'z', 'i', '', 'z', '', 2)
    suo1 = ('suō', 's', 'wo', 'uo', 'u', 'o', '', 1)
    wu2 = ('wú', '', 'wu', 'u', '', 'u', '', 2)
    wo4 = ('wò', '', 'wo', 'uo', 'u', 'o', '', 4)
    wei4 = ('weì', '', 'wei', 'ui', 'u', 'e', 'i', 4)
    ye3 = ('yě', '', 'ye', 'ie', 'i', 'e', '', 3)
    yong1 = ('yōng', '', 'yong', 'iong', 'i', 'o', 'ng', 1)
    yi1 = ('yī', '', 'yi', 'i', '', 'i', '', 1)

    def __new__(
        cls, unicode, consonant, vowel, spell, medial, nucleus, coda, tone
    ):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        obj.unicode = unicode
        obj.consonant = consonant
        obj.vowel = vowel
        obj.spell = spell
        obj.medial = medial
        obj.nucleus = nucleus
        obj.coda = coda
        obj.tone = tone
        return obj

    @classmethod
    def all(cls):
        return [x for x in cls]


@pytest.fixture(
    params=PinyinCase.all(),
    ids=lambda x: x.name
)
def pinyin_case(request):
    return request.param


def test_parse(pinyin_case):
    case = pinyin_case
    pinyin = PinYin(case.unicode)
    assert pinyin.consonant == Consonant.get(case.consonant)
    assert pinyin.vowel.name == case.vowel
    assert pinyin.vowel.spell == case.spell
    assert pinyin.vowel.medial == case.medial
    assert pinyin.vowel.nucleus == case.nucleus
    assert pinyin.vowel.coda == case.coda
    assert pinyin.tone == case.tone


@pytest.mark.parametrize(
    'pinyin, consonants, vowels, tones, expect', [
        ('shuang1', 'FAMILY', 'TRADITIONAL', '1', {
            'fan1',
            'fang1',
            'han1',
            'hang1',
            'huan1',
            'huang1',
            'san1',
            'sang1',
            'shan1',
            'shang1',
            'shuan1',
            'shuang1',
            'suan1',
            'xian1',
            'xiang1',
            'xuan1',
        }),
        ('zhe5', 'ALL_CONSONANTS', 'TRADITIONAL', '5', {
            'e5',
            'de5',
            'ke5',
            'le5',
            'me5',
            'ne5',
            'te5',
            'ze5',
            'zhe5',
        })
    ]
)
def test_rhyme(pinyin, consonants, vowels, tones, expect):
    pinyin = PinYin(pinyin)
    result = set(pinyin.generate_rhymes(consonants, vowels, tones))
    assert result == expect
