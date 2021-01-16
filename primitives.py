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

def create_math_operation(calc_function, num_args):
    # Creates a function that receives num_args arguments and returns the calculated number.
    def math_operation(*args):
        if len(args) != num_args and num_args != -1:
            raise TypeError("Unexpected number of arguments; expected " + str(num_args) + ", received " + str(len(args)))

        operands = convert_to_numbers(args)
        return str(calc_function(*operands))
    return math_operation

def create_word_operation(word_function, num_args):
    # Creates a function that receives num_args arguments and returns the manipulated word.
    def word_operation(*args):
        if len(args) != num_args and num_args != -1:
            raise TypeError("Unexpected number of arguments; expected " + str(num_args) + ", received " + str(len(args)))

        check_word_args(args)
        return word_function(*args)
    return word_operation

def create_reduce_function(action):
    # Returns a function that takes any number of arguments and consecutively applies an action to its arguments, returning a single value
    return (lambda *args: reduce(action, args))

primitives = {
    "+": create_math_operation(create_reduce_function((lambda a, b: a + b)), -1),
    "*": create_math_operation(create_reduce_function((lambda a, b: a * b)), -1),
    "-": create_math_operation(create_reduce_function((lambda a, b: a - b)), -1),
    "/": create_math_operation(create_reduce_function((lambda a, b: a / b)), -1),
    "first": create_word_operation((lambda word: word[0]), 1),
    "last": create_word_operation((lambda word: word[-1]), 1),
    "butfirst": create_word_operation((lambda word: word[1:]), 1),
    "butlast": create_word_operation((lambda word: word[:-1]), 1),
    "quote": (lambda word: word[1:] if word[0] == "'" else word),
    "word": create_word_operation(create_reduce_function((lambda joined_word, next_word: joined_word + next_word)), -1)
}