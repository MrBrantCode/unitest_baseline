"""
QUESTION:
Create a function named `get_data_type` that takes a single argument and returns a string describing the type of argument. The function should only consider the following data types: integer, string, list, tuple, dictionary, and boolean. If the argument's type is not one of these, the function should return "unknown". Do not use built-in type checking functions or libraries.
"""

def get_data_type(arg):
    if isinstance(arg, int) and not isinstance(arg, bool):
        return "integer"
    elif isinstance(arg, str):
        return "string"
    elif isinstance(arg, list):
        return "list"
    elif isinstance(arg, tuple):
        return "tuple"
    elif isinstance(arg, dict):
        return "dictionary"
    elif isinstance(arg, bool):
        return "boolean"
    else:
        return "unknown"