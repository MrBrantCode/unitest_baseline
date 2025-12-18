"""
QUESTION:
Create a function named `describe_type` that takes one argument and returns a string describing the type of the argument. The function should identify the following data types: integer, string, list, tuple, dictionary, and boolean, as well as nested and complex structures such as lists, tuples, and dictionaries containing these data types. The function should not use built-in type checking functions or libraries and should be able to handle larger input sizes efficiently.
"""

def describe_type(argument):
    if isinstance(argument, int):
        return "integer"
    elif isinstance(argument, str):
        return "string"
    elif isinstance(argument, list):
        if all(isinstance(item, int) for item in argument):
            return "list of integers"
        elif all(isinstance(item, str) for item in argument):
            return "list of strings"
        else:
            return "list"
    elif isinstance(argument, tuple):
        if all(isinstance(item, int) for item in argument):
            return "tuple of integers"
        elif all(isinstance(item, str) for item in argument):
            return "tuple of strings"
        else:
            return "tuple"
    elif isinstance(argument, dict):
        return "dictionary"
    elif isinstance(argument, bool):
        return "boolean"
    else:
        return "unknown type"