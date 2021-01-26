import sys
from pytest import raises
sys.path.append('..')
from primitives import primitives, convert_to_numbers

def test_primitive_add():
    # Expects this procedure to add numbers up.
    assert primitives["+"]("1") == "1"
    assert primitives["+"]("1", "2") == "3"
    assert primitives["+"]("1", "2", "3") == "6"

def test_primitive_not_nums():
    # Expects an error if arguments that aren't numbers are sent to procedures that handle numbers
    with raises(TypeError):
        convert_to_numbers(["2", "+"])

def test_primitive_multiply():
    # Expects this procedure to multiply all numbers received.
    assert primitives["*"]("2") == "2"
    assert primitives["*"]("2", "3") == "6"
    assert primitives["*"]("5", "2", "0") == "0"

def test_primitive_subtract():
    # Expects this procedure to subtract all numbers in order.
    assert primitives["-"]("2") == "2"
    assert primitives["-"]("1", "3") == "-2"
    assert primitives["-"]("4", "3", "0") == "1"

def test_primitive_word_operations():
    # Expects these word-manipulating procedures to return the correct values as words
    assert primitives["first"]("foobar") == "f"
    assert primitives["last"]("foobar") == "r"
    assert primitives["butfirst"]("foobar") == "oobar"
    assert primitives["butlast"]("foobar") == "fooba"
    assert primitives["word"]("foo", "bar") == "foobar"
