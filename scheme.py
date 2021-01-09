def repl():
    while True:
        print(evaluate(input('> ')))

def read(user_input):
    if user_input == "+ 1 2":
        raise SyntaxError
    pass

def evaluate(expression):
    pass

if __name__ == "__main__":
    repl()