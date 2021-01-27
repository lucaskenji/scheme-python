def define(*args):
    # Defines a new variable or a new value for an existing variable.
    # First argument for define is the environment it was called, usually global. Second is a name, and third is a value.
    if len(args) != 3:
        raise TypeError("Unexpected number of arguments; expected " + str(len(args)) + ", received " + str(len(args)))
    
    # Variables used for ease of reading
    environment_called = args[0][0]
    variable_name = args[1]
    new_value = args[2]

    environment_called[variable_name] = new_value
    return variable_name

special_forms = {
    "define": define
}