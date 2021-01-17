import sys
sys.path.append('..')
from scheme import get_environment

def test_lookup_same_env():
    assert get_environment("one", ({"one": 1}, None)) == {"one": 1}

def test_lookup_outer_env():
    assert get_environment("one", ({"two": 2}, {"one": 1})) == {"one": 1}