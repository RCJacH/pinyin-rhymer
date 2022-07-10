import pytest

from pinyin_rhymer.consonant import Consonant

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
    return pytest.param(getattr(Consonant, family), x)


def test_hasattr(consonant_cases):
    family, x = consonant_cases.values
    assert hasattr(family, x)


def test_get(consonant_cases):
    family, x = consonant_cases.values
    assert Consonant.get(x) == getattr(family, x)


def test_all():
    all_consonants = {
        x for family in CONSONANT_FAMILIES.values() for x in family
    }
    assert Consonant.all() == all_consonants
    assert len(Consonant.all()) == 21
