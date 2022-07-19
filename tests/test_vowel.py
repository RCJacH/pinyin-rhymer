import pytest

from pinyin_rhymer.error import NotAVowelError
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
        ('ong', 'ong'),
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
        ('van', 'yuan'),
        ('', 'Empty')
    ]
)
def test_parse(pinyin, name):
    assert Vowel(pinyin) == Vowel[name]
    assert eval(repr(Vowel(pinyin))) == Vowel(pinyin)


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
        ('yue', 'ue'),
        ('yun', 'vn'),
        ('yuan', 'van'),
        ('Empty', '')
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
        ('yuan', 'yuan'),
        ('Empty', '')
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
    assert Vowel(original).rhyme('TRADITIONAL') == others


@pytest.mark.parametrize(
    'families', [
        pytest.param({Vowel.a, Vowel.ya, Vowel.wa}, id='1.a'),
        pytest.param({Vowel.e, Vowel.wo}, id='2.wo'),
        pytest.param({Vowel.ye, Vowel.yue}, id='3.ie'),
        pytest.param({Vowel.ai, Vowel.wai}, id='4.ai'),
        pytest.param({Vowel.ei, Vowel.wei}, id='5.ei'),
        pytest.param({Vowel.ao, Vowel.yao}, id='6.ao'),
        pytest.param({Vowel.ou, Vowel.you}, id='7.ou'),
        pytest.param({Vowel.an, Vowel.yan, Vowel.wan, Vowel.yuan}, id='8.an'),
        pytest.param(
            {Vowel.en, Vowel.yin, Vowel.wen, Vowel.yun}, id='9.en|in|un|vn'
        ),
        pytest.param({Vowel.ang, Vowel.yang, Vowel.wang}, id='10.ang'),
        pytest.param(
            {Vowel.eng, Vowel.ying, Vowel.ong, Vowel.yong, Vowel.weng},
            id='11.eng|ing|ong'
        ),
        pytest.param({Vowel.yi, Vowel.yu, Vowel.er}, id='12.i|v|er'),
        pytest.param({Vowel.r, Vowel.z}, id='13.z|r'),
        pytest.param({Vowel.wu}, id='14.u')
    ]
)
def test_similar_fourteen_rhymes(families):
    for each_vowel in families:
        assert each_vowel.rhyme('FOURTEEN_RHYMES') == families


@pytest.mark.parametrize(
    'original, others', [
        ('e', {Vowel.e, Vowel.er}),
        ('a', {
            Vowel.a,
            Vowel.ya,
            Vowel.wa,
            Vowel.ai,
            Vowel.wai,
            Vowel.ao,
            Vowel.yao,
            Vowel.ang,
            Vowel.yang,
            Vowel.wang,
        }),
        ('ei', {
            Vowel.ei,
            Vowel.wei,
            Vowel.en,
            Vowel.wen,
            Vowel.ye,
            Vowel.yue
        }),
        ('ou', {
            Vowel.ou, Vowel.you, Vowel.ong, Vowel.yong, Vowel.wo
        }),
        ('u', {
            Vowel.wu
        })
    ]
)
def test_similar_body(original, others):
    assert Vowel(original).rhyme('SIMILAR_BODY') == others


@pytest.mark.parametrize(
    'original, others', [
        ('e', {Vowel.e}),
        ('a', {Vowel.a, Vowel.ya, Vowel.wa}),
        ('ai', {Vowel.ai, Vowel.wai, Vowel.yi, Vowel.ei, Vowel.wei}),
        ('ou', {
            Vowel.ou,
            Vowel.ao,
            Vowel.yao,
            Vowel.you,
            Vowel.wu
        }),
        ('an', {
            Vowel.an,
            Vowel.yan,
            Vowel.wan,
            Vowel.yuan,
            Vowel.en,
            Vowel.wen,
            Vowel.yin,
            Vowel.yun
        }),
        ('ang', {
            Vowel.ang,
            Vowel.yang,
            Vowel.wang,
            Vowel.eng,
            Vowel.weng,
            Vowel.ying,
            Vowel.ong,
            Vowel.yong
        }),
        (
            'ye', {
                Vowel.ye,
                Vowel.yue
            }
        )
    ]
)
def test_similar_tail(original, others):
    assert Vowel(original).rhyme('SIMILAR_TAIL') == others


@pytest.mark.parametrize(
    'original, others', [
        ('e', {Vowel.e, Vowel.r, Vowel.er}),
        ('a', {Vowel.a}),
        ('ei', {Vowel.ei}),
        ('ai', {Vowel.ai}),
        ('ou', {Vowel.ou}),
        ('ao', {Vowel.ao}),
        ('en', {Vowel.en}),
        ('an', {Vowel.an}),
        ('eng', {Vowel.eng, Vowel.ong}),
        ('ang', {Vowel.ang}),
        ('you', {Vowel.you}),
    ]
)
def test_similar_sounding(original, others):
    assert Vowel[original].similar_sounding() == others


@pytest.mark.parametrize(
    'original, threshold, others', [
        ('ao', 0.4, {Vowel.ao, Vowel.ou}),
        ('u', 0.4, {Vowel.wu, Vowel.r, Vowel.er})
    ]
)
def test_similar_sounding_with_threshold(original, threshold, others):
    assert Vowel(original).similar_sounding(threshold=threshold) == others


@pytest.mark.parametrize(
    'families', [
        {
            Vowel.a,
            Vowel.e,
            Vowel.er,
            Vowel.yi,
            Vowel.z,
            Vowel.r,
            Vowel.wu,
            Vowel.yu
        },
        {
            Vowel.ei,
            Vowel.ai,
            Vowel.wei,
            Vowel.wai
        },
        {
            Vowel.an,
            Vowel.en,
            Vowel.yan,
            Vowel.wan,
            Vowel.wen,
            Vowel.yuan,
            Vowel.ou,
            Vowel.you
        },
        {
            Vowel.ang,
            Vowel.yang,
            Vowel.yin,
            Vowel.yao,
            Vowel.weng,
            Vowel.wang,
            Vowel.ong,
            Vowel.yun,
            Vowel.ao,
            Vowel.eng,
            Vowel.yong,
        }
    ]
)
def test_similar_mouth_movement(families):
    for vowel in families:
        assert vowel.rhyme('SIMILAR_MOUTH_MOVEMENT') == families


@pytest.mark.parametrize(
    'original, others', [
        ('e', {Vowel.e}),
        ('a', {
            Vowel.a,
            Vowel.ai,
            Vowel.ao,
            Vowel.an,
            Vowel.ya,
            Vowel.wa,
        }),
        ('ei', {Vowel.ei, Vowel.wei}),
        ('ai', {Vowel.ai, Vowel.wai}),
        ('ou', {Vowel.ou, Vowel.you}),
        ('ao', {Vowel.ao, Vowel.yao}),
        ('en', {Vowel.en, Vowel.eng, Vowel.wen}),
        ('an', {
            Vowel.an,
            Vowel.ang,
            Vowel.yan,
            Vowel.wan,
            Vowel.yuan
        }),
        ('eng', {Vowel.eng, Vowel.weng}),
        ('ang', {Vowel.ang, Vowel.yang, Vowel.wang}),
        ('yi', {Vowel.yi, Vowel.ye, Vowel.ya, Vowel.yin}),
        ('ya', {Vowel.ya, Vowel.yao, Vowel.yan}),
        ('wu', {Vowel.wu, Vowel.wo, Vowel.wa}),
        ('yu', {Vowel.yu, Vowel.yue, Vowel.yun})
    ]
)
def test_similar_additive(original, others):
    assert Vowel(original).rhyme('ADDITIVE') == others


@pytest.mark.parametrize(
    'original, others', [
        ('e', {Vowel.e}),
        ('a', {Vowel.a}),
        ('ei', {Vowel.ei}),
        ('ai', {Vowel.ai, Vowel.a}),
        ('ou', {Vowel.ou}),
        ('ao', {Vowel.ao, Vowel.a}),
        ('en', {Vowel.en}),
        ('an', {Vowel.an, Vowel.a}),
        ('eng', {Vowel.eng, Vowel.en}),
        ('ang', {Vowel.ang, Vowel.an}),
        ('yi', {Vowel.yi}),
        ('ye', {Vowel.ye, Vowel.yi}),
        ('ya', {Vowel.ya, Vowel.yi, Vowel.a}),
        ('you', {Vowel.you, Vowel.ou}),
        ('yao', {Vowel.yao, Vowel.ya, Vowel.ao}),
        ('ying', {Vowel.ying, Vowel.yin}),
        ('yang', {Vowel.yang, Vowel.yan, Vowel.ang}),
        ('wo', {Vowel.wo, Vowel.wu}),
        ('wa', {Vowel.wa, Vowel.wu, Vowel.a}),
        ('wei', {Vowel.wei, Vowel.ei}),
        ('wai', {Vowel.wai, Vowel.wa, Vowel.ai}),
        ('weng', {Vowel.weng, Vowel.wen, Vowel.eng}),
        ('wang', {Vowel.wang, Vowel.wan, Vowel.ang}),
        ('yue', {Vowel.yue, Vowel.yu}),
        ('yun', {Vowel.yun, Vowel.yu}),
        ('yuan', {Vowel.yuan, Vowel.an}),
    ]
)
def test_similar_subtractive(original, others):
    assert Vowel(original).rhyme('SUBTRACTIVE') == others


def test_not_a_vowel_error():
    with pytest.raises(NotAVowelError) as excinfo:
        Vowel('not a vowel')
    assert 'not a vowel' in str(excinfo.value)
