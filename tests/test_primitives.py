import sys
from pytest import raises
sys.path.append('..')
from primitives import primitives

def test_primitive_add():
    assert primitives["+"]("1") == "1"
    assert primitives["+"]("1", "2") == "3"
    assert primitives["+"]("1", "2", "3") == "6"

def test_primitive_bad_add():
    with raises(TypeError):
        primitives["+"]("2", "+")