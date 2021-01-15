from functools import reduce

def convert_to_numbers(argument_list):
    # Converts a list of string numbers into actual numbers.
    try:
        converted_args = list(map(lambda x: float(x) if "." in x else int(x), argument_list))
    except ValueError:
        raise TypeError("Expected number arguments, received string")

    return converted_args

def check_word_args(argument_list):
    pass

def create_basic_operation(calc_function):
    # Creates a function that receives arguments, applies calc_function consecutively and returns the result as string
    def basic_operation(*args):
        operands = convert_to_numbers(args)
        return str(reduce(calc_function, operands))
    return basic_operation

def division(*args):
    try:
        return create_basic_operation((lambda a, b: a / b))(*args)
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide a number by zero.")

primitives = {
    "+": create_basic_operation((lambda a, b: a + b)),
    "*": create_basic_operation((lambda a, b: a * b)),
    "-": create_basic_operation((lambda a, b: a - b)),
    "/": division
}