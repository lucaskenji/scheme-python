from primitives import primitives

def repl():
    # Read-eval-print-loop: loops until the program is exited. Receives user input and returns the result of the expression
    while True:
        print(evaluate(read(input('> '))))

def read(user_input):
    # Reads user input (expecting Scheme lists) and returns it as Python lists.
    # (+ 1 2) ==> ['+', '1', '2']

    if len(user_input) == 1:
        # Edge case, '+' should be later evaluated to 'PrimitiveProcedure', etc.
        return [user_input]

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
                if current_argument[0] == "'":
                    # Arguments starting with a quote(') are transformed into (quote argument)
                    current_list.append(["quote", current_argument])
                else:
                    current_list.append(current_argument)
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
                if current_argument[0] == "'":
                    # Arguments starting with a quote(') are transformed into (quote argument)
                    current_list.append(["quote", current_argument])
                else:
                    current_list.append(current_argument)
                current_argument = ""
        else:
            # Continues reading the argument
            current_argument += character
    
    if len(parenthesis_stack) != 0:
        # Every opening parenthesis needs a closing parenthesis to be popped from the stack.
        raise SyntaxError("Parentheses did not match up!")
    
    if current_argument:
        # Usually will happen when the user input does not end with a parenthesis.
        raise SyntaxError("Unexpected end of expression while reading")
    
    # Must remove result from two arrays. The outermost one is needed for the stack implementation as an array.
    # The other one isn't necessarily needed, but it's more convenient than handling the error cases that come without it. 
    [[parsed_exp]] = nested_stack
    return parsed_exp

def evaluate(expression):
    # Receives an expression and returns its result
    # ["+", "1", "2"] ==> "3"
    
    # Lists of length one evaluate to the single value inside
    if len(expression) == 1:
        return expression[0]
    
    # Lists of other lengths are considered procedure calls
    # The anonymous function below ensures evaluate will always receive a list
    argument_list = list(map(lambda arg: arg if isinstance(arg, list) else [arg], expression[1:]))

    # When receiving a procedure call, returns the result of the function applied with the evaluated arguments
    return apply(expression[0], list(map(evaluate, argument_list)))

def apply(procedure, arguments):
    # Receives a procedure with its arguments and return the result of the applied function
    if procedure in primitives:
        return primitives[procedure](*arguments)
    else:
        # This part would include the user defined functions
        return NotImplementedError

if __name__ == "__main__":
    repl()