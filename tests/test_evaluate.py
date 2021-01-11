import sys
from pytest import raises
sys.path.append('..')
from scheme import evaluate

def test_eval_single():
    # Expects single values to be evaluated
    assert evaluate(["+"]) == "+"
    assert evaluate(["1"]) == "1"

def test_eval_proc_call():
    # Expects a list to be evaluated as a procedure call
    assert evaluate(["+", "1", "2"]) == "3"

def test_eval_bad_call():
    # Expects an error if the procedure called has a problem in its operands(in this case, the addition operator cannot add procedures)
    with raises(TypeError):
        evaluate(["+", "3", "+"])

def test_eval_nested_call():
    # Expects a list containing a list to be successfully evaluated in applicative order
    assert evaluate(["+", ["*", "2", "3"], "1"]) == "7"