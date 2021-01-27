from primitives import primitives
from special_forms import special_forms

global_env = ({**primitives, **special_forms}, None)

def repl():
    # Read-eval-print-loop: loops until the program is exited. Receives user input and returns the result of the expression
    while True:
        print(evaluate(read(input('> ')), global_env))

def read(user_input):
    # Reads user input (expecting Scheme lists) and returns it as Python lists.
    # (+ 1 2) ==> ['+', '1', '2']

    nested_stack = [] # TODO: abstract into stack. Used to handle nested expressions.
    current_list = []
    parenthesis_stack = [] # TODO: abstract into stack.
    current_argument = "" # Used to read each element inside a pair of parentheses, until a whitespace or closing parenthesis is reached.

    # current_list stores a reference to the actual list, so it's possible to add it to the stack beforehand.
    nested_stack.append(current_list)

    for character in user_input:
        if character == '(':
            # Adds parenthesis to stack to check if it closes later.
            parenthesis_stack.append('(')
            current_list = []
            nested_stack.append(current_list)
        elif character == ')':
            if current_argument:
                # Stops reading an argument when encountering a closed parenthesis.
                if current_argument == '"' == current_list[-1]:
                    # Treats " " as a space
                    current_list[-1] = " "
                else:
                    current_list.append(read_argument(current_argument))
                current_argument = ""
            
            try:
                if parenthesis_stack[-1] == '(':
                    parenthesis_stack.pop()
                    subexp = nested_stack.pop()
                    nested_stack[-1].append(subexp)
                    current_list = nested_stack[-1]
                else:
                    raise SyntaxError("Parenthesis did not have a pair.")
            except IndexError:
                # Specific to the parenthesis_stack[-1], that can return an IndexError when empty.
                # Could potentially be raised by nested_stack[-1], but I don't see it happening.
                raise SyntaxError("Attempted to close parenthesis before opening it")
        elif character == ' ':
            if current_argument:
                # Stops reading an argument when encountering a space.
                if current_argument == '"' == current_list[-1]:
                    # Treats " " as a space
                    current_list[-1] = " "
                else:
                    current_list.append(read_argument(current_argument))
                current_argument = ""
        else:
            # Continues reading the argument
            current_argument += character
    
    if len(parenthesis_stack) != 0:
        # Every opening parenthesis needs a closing parenthesis to be popped from the stack.
        raise SyntaxError("Parentheses did not match up!")
    
    if current_argument:
        # Usually will happen when the user input does not end with a parenthesis.
        if nested_stack == [[]]:
            return [current_argument]
        else:
            raise SyntaxError("Unexpected end of expression while reading")
    
    # Must remove result from two arrays. The outermost one is needed for the stack implementation as an array.
    # The other one isn't necessarily needed, but it's more convenient than handling the error cases that come without it. 
    [[parsed_exp]] = nested_stack
    return parsed_exp

def read_argument(arg):
    # Reads an argument starting with ' as (quote argument), otherwise just returns the argument
    if arg[0] == "'":
        return ["quote", arg]
    else:
        return arg

def evaluate(expression, environment):
    # Receives an expression to evaluate in a given environment and returns its result
    # ["+", "1", "2"] ==> "3"

    # Will be used to identify if we are evaluating a defined procedure
    firstexp_environment = get_environment(expression[0], environment)

    if len(expression) == 1:
        if firstexp_environment is not None:
            return firstexp_environment[0][expression[0]]
        
        return expression[0]
    
    # More than 1 element on the list; considered a procedure call
    argument_list = list(map(lambda arg: arg if isinstance(arg, list) else [arg], expression[1:]))
    procedure_called = expression[0] if isinstance(expression[0], list) else [expression[0]]

    if firstexp_environment is None:
        raise NameError("Unbound procedure " + expression[0])

    # Special forms like "define" are applied on a different function
    if expression[0] in special_forms:
        return apply_special_form(procedure_called, argument_list, environment)
    else:
        return apply(evaluate(procedure_called, environment), list(map(lambda arg: evaluate(arg, firstexp_environment), argument_list)))

def apply(procedure, arguments):
    return procedure(*arguments)

def apply_special_form(procedure, arguments, env):
    if procedure[0] == "define":
        variable_name = arguments[0][0]
        evaluated_args = list(map(lambda arg: evaluate(arg, env), arguments[1:]))
        return evaluate(procedure, env)(env, variable_name, *evaluated_args)
    else:
        raise NotImplementedError

def get_environment(name, env):
    # Searches an assigned value for a given name. If not found, tries again on an enclosing environment, until it reaches the global env.
    if name in env[0]:
        return env
    
    if env == global_env:
        return None
    
    return get_environment(name, env[1])

if __name__ == "__main__":
    repl()