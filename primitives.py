from functools import reduce

def add(*args):
    operands = []
    try:
        for operand in args:
            operands.append(int(operand))
    except ValueError:
        raise TypeError("All arguments to '+' must be numbers.")
    return str(reduce(lambda a, b: a + b, operands))

def multiply(*args):
    operands = []
    try:
        for operand in args:
            operands.append(int(operand))
    except ValueError:
        raise TypeError("All arguments to '*' must be numbers.")
    return str(reduce(lambda a, b: a * b, operands))

primitives = {
    "+": add,
    "*": multiply
}