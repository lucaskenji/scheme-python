import sys
from pytest import raises
sys.path.append('..')
from scheme import read

def test_read_simple():
    # Expects expressions to be read correctly
    assert read("(+ 1 2)") == ["+", 1, 2]

def test_read_nested():
    # Expects nested expressions to be read as nested lists
    assert read("(+ (* 2 3) 1)") == ["+", ["*", 2, 3], 1]

def test_read_proc():
    # Expects single values to be accepted without parenthesis
    assert read("+") == ["PrimitiveProcedure"]

def test_read_number():
    # Expects single values to be accepted without parenthesis
    assert read("1") == [1]

def test_read_bad_exp():
    # Expects the user input to be a list(i.e with parenthesis on both sides).
    with raises(SyntaxError):
        read("+ 1 2")