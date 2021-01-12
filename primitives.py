from functools import reduce

def convert_to_numbers(argument_list):
    try:
        converted_args = list(map(lambda x: float(x) if "." in x else int(x), argument_list))
    except ValueError:
        raise TypeError("Expected number arguments, received string")
        
    return converted_args

def add(*args):
    operands = convert_to_numbers(args)
    return str(reduce(lambda a, b: a + b, operands))

def multiply(*args):
    operands = convert_to_numbers(args)
    return str(reduce(lambda a, b: a * b, operands))

primitives = {
    "+": add,
    "*": multiply
}