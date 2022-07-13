import pytest

from pinyin_rhymer.consonant import Consonant, ConsonantFamily
from pinyin_rhymer.error import NotAConsonantError

CONSONANT_FAMILIES = {
    'Plosives': 'p t k b d g'.split(),
    'Fricatives': 'f x h s sh'.split(),
    'Affricates': 'j q z zh c ch'.split(),
    'Laterals': 'l r'.split(),
    'Nasals': 'm n'.split()
}


@pytest.fixture(
    params=((family, x) for family in CONSONANT_FAMILIES
            for x in CONSONANT_FAMILIES[family]),
    ids=lambda x: '_'.join(x)
)
def consonant_cases(request):
    family, x = request.param
    return family, x


def test_empty():
    assert str(Consonant.Empty) == ''
    assert Consonant('') == ''


def test_get(consonant_cases):
    family, x = consonant_cases
    assert Consonant(x) == x
    assert Consonant(x).family == ConsonantFamily(family)


@pytest.mark.parametrize(
    'this, other', [('Z', 'zh'), ('S', 'sh'), ('C', 'ch')]
)
def test_zhchsh_translation(this, other):
    assert Consonant(this) == Consonant(other)


def test_all():
    all_consonants = {
        x for family in CONSONANT_FAMILIES.values() for x in family
    }
    all_consonants.add('')
    assert {str(x) for x in Consonant.all()} == all_consonants
    assert Consonant.all_as_str() == all_consonants
    assert len(Consonant.all()) == 22
    assert len(Consonant.all()) == 22


def test_not_a_consonant_error():
    with pytest.raises(NotAConsonantError) as excinfo:
        Consonant('not a consonant')
    assert 'not a consonant' in str(excinfo.value)
