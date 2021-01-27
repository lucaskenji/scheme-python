import sys
from pytest import raises
sys.path.append('..')
from special_forms import special_forms

def test_define_bad_args():
    # Expects an error if define is called with wrong number of arguments
    with raises(TypeError):
        special_forms["define"]("a", "b", "c", "d")

def test_define_new_var():
    # Expects a new variable to be defined if it doesn't exist
    test_env = ({"a": "1"}, None)
    special_forms["define"](test_env, "b", "3")
    assert test_env[0]["b"] == "3"

def test_define_assign():
    # Expects a new value to be assigned into a previously defined variable
    test_env = ({"a": "1"}, None)
    special_forms["define"](test_env, "a", "3")
    assert test_env[0]["a"] == "3"