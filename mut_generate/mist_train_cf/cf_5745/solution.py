"""
QUESTION:
Create a function called `describe_type` that takes one argument and returns a string describing the type of the argument. The function should consider the following data types: integer, string, list, tuple, dictionary, and boolean. It should also correctly identify and describe more complex data structures such as nested lists, nested tuples, and nested dictionaries, and handle combinations of different data types within these complex structures. The function should not use any built-in type checking functions or libraries, and should handle larger input sizes efficiently.
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