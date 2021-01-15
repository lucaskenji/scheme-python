from functools import reduce

def convert_to_numbers(argument_list):
    # Converts a list of string numbers into actual numbers.
    try:
        converted_args = list(map(lambda x: float(x) if "." in x else int(x), argument_list))
    except ValueError:
        raise TypeError("Expected number arguments, received string")

    return converted_args

def check_word_args(argument_list):
    # Checks if a list of word arguments has any numbers and, if it does, raises an exception
    for arg in argument_list:
        try:
            float(arg)
            raise TypeError("Expected word arguments, received number")
        except ValueError:
            continue

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

def create_word_slicer(slice_function):
    # Creates a function that receives one word as argument and returns a part of it(determined by slice_function).
    def word_slicer(*args):
        if len(args) != 1:
            raise TypeError("This function takes exactly one argument; " + str(len(args)) + " given")

        check_word_args(args)
        return slice_function(*args)
    return word_slicer

primitives = {
    "+": create_basic_operation((lambda a, b: a + b)),
    "*": create_basic_operation((lambda a, b: a * b)),
    "-": create_basic_operation((lambda a, b: a - b)),
    "/": division,
        # The four functions below ensure that the string is returned with a quote(') to represent a word.
    "first": create_word_slicer((lambda word: word[:2])),
    "last": create_word_slicer((lambda word: "'" + word[-1])),
    "butfirst": create_word_slicer((lambda word: "'" + word[2:])),
    "butlast": create_word_slicer((lambda word: word[:-1]))
}