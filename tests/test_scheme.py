import sys
sys.path.append('..')
from scheme import read

def test_read_simple():
    assert read("(+ 1 2)") == ["+", 1, 2]

def test_read_nested():
    assert read("(+ (* 2 3) 1)") == ["+", ["*", 2, 3], 1]

def test_read_proc():
    assert read("+") == ["PrimitiveProcedure"]

def test_read_number():
    assert read("1") == [1]