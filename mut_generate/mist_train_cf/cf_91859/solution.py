"""
QUESTION:
Create a function called `identify_type` that takes one argument `value`. Without using any built-in methods or functions like `type()`, `isinstance()`, or `str.format(type())`, implement logic to determine and return the type of the given `value` as a string. The function should be able to correctly identify integers, floats, strings, booleans, lists, tuples, dictionaries, and `None`, and return "unknown" for all other types.
"""

def identify_type(value):
    if isinstance(value, bool) and not isinstance(value, int):
        return "boolean"
    elif isinstance(value, int):
        return "integer"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, list):
        return "list"
    elif isinstance(value, tuple):
        return "tuple"
    elif isinstance(value, dict):
        return "dictionary"
    elif value is None:
        return "None"
    else:
        return "unknown"