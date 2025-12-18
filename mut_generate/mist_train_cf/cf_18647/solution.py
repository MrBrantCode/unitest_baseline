"""
QUESTION:
Create a function `is_integer(variable)` that determines whether a given variable represents an integer, without using any built-in functions or libraries for type checking. The function should handle edge cases such as variables that are strings or floats representing integers, booleans representing integers, and nested data structures like lists, tuples, and dictionaries. Additionally, the function should be optimized for performance and handle cases where the input variable is a complex number, a byte object, or a custom user-defined object that represents an integer.
"""

def is_integer(variable):
    if isinstance(variable, int):
        return True
    elif isinstance(variable, str):
        if variable.isdigit():
            return True
        try:
            int(variable)
            return True
        except ValueError:
            return False
    elif isinstance(variable, float):
        return variable == round(variable)
    elif isinstance(variable, bool):
        return variable in [0, 1]
    elif isinstance(variable, list) or isinstance(variable, tuple):
        for element in variable:
            if not is_integer(element):
                return False
        return True
    elif isinstance(variable, dict):
        for value in variable.values():
            if not is_integer(value):
                return False
        return True
    else:
        return False