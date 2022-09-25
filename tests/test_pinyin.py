from enum import Enum

import pytest

from pinyin_rhymer.consonant import Consonant
from pinyin_rhymer.error import NotAPinYinError
from pinyin_rhymer.pinyin import PinYin
from pinyin_rhymer.vowel import Vowel


class PinyinCase(Enum):
    a5 = ('a', '', 'a', 'a', '', 'a', '', 5)
    bo3 = ('bǒ', 'b', 'wo', 'uo', 'u', 'o', '', 3)
    pu1 = ('pū', 'p', 'wu', 'u', '', 'u', '', 1)
    ming3 = ('mǐng', 'm', 'ying', 'ing', '', 'i', 'ng', 3)
    fen2 = ('fén', 'f', 'en', 'en', '', 'ə', 'n', 2)
    dai4 = ('dài', 'd', 'ai', 'ai', '', 'a', 'i', 4)
    tu1 = ('tū', 't', 'wu', 'u', '', 'u', '', 1)
    nv3 = ('nǚ', 'n', 'yu', 'v', '', 'v', '', 3)
    liu2 = ('liú', 'l', 'you', 'iu', 'i', 'o', 'u', 2)
    gang4 = ('gàng', 'g', 'ang', 'ang', '', 'a', 'ng', 4)
    ke3 = ('kě', 'k', 'e', 'e', '', 'ɤ', '', 3)
    hui2 = ('huí', 'h', 'wei', 'ui', 'u', 'e', 'i', 2)
    jue1 = ('juē', 'j', 'yue', 'ue', 'v', 'e', '', 1)
    jiu3 = ('jiǔ', 'j', 'you', 'iu', 'i', 'o', 'u', 3)
    qu4 = ('qù', 'q', 'yu', 'v', '', 'v', '', 4)
    xie2 = ('xié', 'x', 'ye', 'ie', 'i', 'e', '', 2)
    zhao1 = ('zhāo', 'zh', 'ao', 'ao', '', 'a', 'u', 1)
    chuang1 = ('chuāng', 'ch', 'wang', 'uang', 'u', 'a', 'ng', 1)
    shi4 = ('shì', 'sh', 'r', 'i', '', 'r', '', 4)
    rou3 = ('rǒu', 'r', 'ou', 'ou', '', 'o', 'u', 3)
    zan4 = ('zàn', 'z', 'an', 'an', '', 'a', 'n', 4)
    zong4 = ('zòng', 'z', 'ong', 'ong', '', 'o', 'ng', 4)
    ci2 = ('cí', 'c', 'z', 'i', '', 'z', '', 2)
    cun1 = ('cūn', 'c', 'wen', 'un', 'u', 'ə', 'n', 1)
    suo1 = ('suō', 's', 'wo', 'uo', 'u', 'o', '', 1)
    wu2 = ('wú', '', 'wu', 'u', '', 'u', '', 2)
    wo4 = ('wò', '', 'wo', 'uo', 'u', 'o', '', 4)
    wei4 = ('wèi', '', 'wei', 'ui', 'u', 'e', 'i', 4)
    ye3 = ('yě', '', 'ye', 'ie', 'i', 'e', '', 3)
    yong1 = ('yōng', '', 'yong', 'iong', 'i', 'o', 'ng', 1)
    yi1 = ('yī', '', 'yi', 'i', '', 'i', '', 1)
    er3 = ('ěr', '', 'er', 'er', '', 'ɚ', '', 3)

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
    assert pinyin.consonant == Consonant(case.consonant)
    assert pinyin.vowel.name == case.vowel
    assert pinyin.vowel.spell == case.spell
    assert pinyin.vowel.medial == case.medial
    assert pinyin.vowel.nucleus == case.nucleus
    assert pinyin.vowel.coda == case.coda
    assert pinyin.tone == case.tone
    assert eval(repr(pinyin)) == pinyin


def test_parse_alternative():
    pinyin = PinYin('a4')
    other = PinYin(pinyin)
    assert pinyin == other


def test_with_tone_mark(pinyin_case):
    case = pinyin_case
    pinyin = PinYin(case.name)
    assert pinyin.with_tone_mark() == case.unicode


def test_equal(pinyin_case):
    pinyin = PinYin(pinyin_case.name)
    assert hash(pinyin) == hash(pinyin_case.unicode)
    assert pinyin == pinyin_case.name


@pytest.mark.parametrize(
    'pinyin, consonants, vowels, tones, expect', [
        ('shuang1', 'FAMILY', 'FOURTEEN_RHYMES', '1', {
            'fang1',
            'hang1',
            'huang1',
            'sang1',
            'shang1',
            'shuang1',
            'xiang1',
        }),
        ('zhe5', 'ALL', 'SIMILAR_BODY', '5', {
            'e5',
            'de5',
            'ke5',
            'le5',
            'me5',
            'ne5',
            'te5',
            'ze5',
            'zhe5',
        }),
        ('shei2', 'fSs', 'FOURTEEN_RHYMES', '2', {
            'shei2',
            'fei2',
            'sui2',
            'shui2'
        })
    ]
)
def test_generate_rhymes(pinyin, consonants, vowels, tones, expect):
    pinyin = PinYin(pinyin)
    result = set(map(str, pinyin.generate_rhymes(consonants, vowels, tones)))
    assert result == expect


@pytest.mark.parametrize(
    'this, other, options', [
        ('a4', 'ba4', [])
    ]
)
def test_rhymes_with(this, other, options):
    pinyin = PinYin(this)
    assert pinyin.rhymes_with(other, *options)


@pytest.mark.parametrize(
    'input', [
        'not a pinyin',
        'wah3',
        'bar',
    ]
)
def test_not_a_pinyin_error(input):
    with pytest.raises(NotAPinYinError) as excinfo:
        PinYin(input)
    assert input in str(excinfo.value)


def test_valid_pinyin(pinyin_case):
    assert PinYin(
        pinyin_case.consonant, pinyin_case.vowel, pinyin_case.tone
    ).is_valid


@pytest.mark.parametrize(
    'pinyin_parts', [
        (Consonant.b, Vowel.r, 4),
        (Consonant.b, Vowel.yong, 3),
        (Consonant.j, Vowel.wu, 1),
        (Consonant.x, Vowel.wu, 2),
    ]
)
def test_invalid_pinyin(pinyin_parts):
    assert PinYin(*pinyin_parts).is_valid is False
