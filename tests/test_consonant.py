import pytest

from pinyin_rhymer.consonant import Consonant
from pinyin_rhymer.error import NotAConsonantError

CONSONANT_FAMILIES = {
    'Plosive': 'p t k b d g'.split(),
    'Fricative': 'f x h s sh'.split(),
    'Affricate': 'j q z zh c ch'.split(),
    'Lateral': 'l r'.split(),
    'Nasal': 'm n'.split()
}


@pytest.fixture(
    params=((family, x) for family in CONSONANT_FAMILIES
            for x in CONSONANT_FAMILIES[family]),
    ids=lambda x: '_'.join(x)
)
def consonant_cases(request):
    family, x = request.param
    return pytest.param(Consonant[family], x)


def test_hasattr(consonant_cases):
    family, x = consonant_cases.values
    assert hasattr(family, x)


def test_get(consonant_cases):
    family, x = consonant_cases.values
    assert Consonant.get(x) == family[x]


def test_all():
    all_consonants = {
        x for family in CONSONANT_FAMILIES.values() for x in family
    }
    all_consonants.add('')
    assert Consonant.all() == all_consonants
    assert len(Consonant.all()) == 22


def test_not_a_consonant_error():
    with pytest.raises(NotAConsonantError) as excinfo:
        Consonant.get('not a consonant')
    assert 'not a consonant' in str(excinfo.value)
