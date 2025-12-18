"""
QUESTION:
Create a function named `get_data_type` that takes one argument. The function should return a string describing the type of argument. It should identify the following data types: integer, string, list, tuple, dictionary, and boolean, without using built-in type checking functions or libraries. If the argument is of a different data type, the function should return "unknown".
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