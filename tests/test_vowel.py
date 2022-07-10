import pytest

from pinyin_rhymer.vowel import Vowel


@pytest.mark.parametrize(
    ('pinyin, name'), [
        ('e', 'e'),
        ('a', 'a'),
        ('ei', 'ei'),
        ('ai', 'ai'),
        ('ou', 'ou'),
        ('ao', 'ao'),
        ('en', 'en'),
        ('an', 'an'),
        ('eng', 'eng'),
        ('ang', 'ang'),
        ('er', 'er'),
        ('z', 'z'),
        ('r', 'r'),
        ('i', 'yi'),
        ('ie', 'ye'),
        ('ia', 'ya'),
        ('iu', 'you'),
        ('iao', 'yao'),
        ('in', 'yin'),
        ('yin', 'yin'),
        ('ian', 'yan'),
        ('ing', 'ying'),
        ('iong', 'yong'),
        ('iang', 'yang'),
        ('u', 'wu'),
        ('uo', 'wo'),
        ('ua', 'wa'),
        ('ui', 'wei'),
        ('uai', 'wai'),
        ('wen', 'wen'),
        ('uan', 'wan'),
        ('weng', 'weng'),
        ('uang', 'wang'),
        ('v', 'yu'),
        ('ve', 'yue'),
        ('vn', 'yun'),
        ('van', 'yuan')
    ]
)
def test_parse(pinyin, name):
    assert Vowel(pinyin) == Vowel[name]


@pytest.mark.parametrize(
    'name, pinyin', [
        ('e', 'e'),
        ('yi', 'i'),
        ('z', 'i'),
        ('r', 'i'),
        ('ye', 'ie'),
        ('ya', 'ia'),
        ('you', 'iu'),
        ('yao', 'iao'),
        ('yin', 'in'),
        ('yan', 'ian'),
        ('ying', 'ing'),
        ('yong', 'iong'),
        ('yang', 'iang'),
        ('wu', 'u'),
        ('wo', 'uo'),
        ('wa', 'ua'),
        ('wei', 'ui'),
        ('wai', 'uai'),
        ('wen', 'un'),
        ('wan', 'uan'),
        ('weng', 'weng'),
        ('wang', 'uang'),
        ('yu', 'v'),
        ('yue', 've'),
        ('yun', 'vn'),
        ('yuan', 'van')
    ]
)
def test_with_consonant(name, pinyin):
    assert Vowel[name].with_consonant == pinyin


@pytest.mark.parametrize(
    'name, pinyin', [
        ('e', 'e'),
        ('yi', 'yi'),
        ('z', 'yi'),
        ('r', 'yi'),
        ('ye', 'ye'),
        ('ya', 'ya'),
        ('you', 'you'),
        ('yao', 'yao'),
        ('yin', 'yin'),
        ('yan', 'yan'),
        ('ying', 'ying'),
        ('yong', 'yong'),
        ('yang', 'yang'),
        ('wu', 'wu'),
        ('wo', 'wo'),
        ('wa', 'wa'),
        ('wei', 'wei'),
        ('wai', 'wai'),
        ('wen', 'wen'),
        ('wan', 'wan'),
        ('weng', 'weng'),
        ('wang', 'wang'),
        ('yu', 'yu'),
        ('yue', 'yue'),
        ('yun', 'yun'),
        ('yuan', 'yuan')
    ]
)
def test_without_consonant(name, pinyin):
    assert Vowel[name].without_consonant == pinyin


@pytest.mark.parametrize(
    'original, others', [
        ('e', {Vowel.e}),
        ('a', {Vowel.a, Vowel.ya, Vowel.wa}),
        ('ei', {Vowel.ei, Vowel.wei}),
        ('ai', {Vowel.ai, Vowel.wai}),
        ('ou', {Vowel.ou, Vowel.you}),
        ('ao', {Vowel.ao, Vowel.yao}),
        ('en', {Vowel.en, Vowel.wen, Vowel.eng, Vowel.weng}),
        ('an', {
            Vowel.an,
            Vowel.yan,
            Vowel.wan,
            Vowel.yuan,
            Vowel.ang,
            Vowel.yang,
            Vowel.wang
        }),
        ('eng', {Vowel.eng, Vowel.weng, Vowel.en, Vowel.wen}),
        ('ang', {
            Vowel.ang,
            Vowel.yang,
            Vowel.wang,
            Vowel.an,
            Vowel.yan,
            Vowel.wan,
            Vowel.yuan
        }),
        ('ye', {Vowel.ye, Vowel.yue}),
    ]
)
def test_similar_traditional(original, others):
    assert Vowel[original].similar_traditional() == others


@pytest.mark.parametrize(
    'original, others', [
        ('e', {Vowel.e, Vowel.r, Vowel.er}),
        ('a', {Vowel.a}),
        ('ei', {Vowel.ei}),
        ('ai', {Vowel.ai}),
        ('ou', {Vowel.ou, Vowel.ao}),
        ('ao', {Vowel.ao, Vowel.ou}),
        ('en', {Vowel.en}),
        ('an', {Vowel.an}),
        ('eng', {Vowel.eng}),
        ('ang', {Vowel.ang}),
        ('you', {Vowel.you, Vowel.yao}),
    ]
)
def test_similar_sounding(original, others):
    assert Vowel[original].similar_sounding() == others
