"""
QUESTION:
Write a function called `variable_type` that determines the type of a given value. The function should return 'integer' if the value is an integer, 'float' if it's a floating-point number, and 'string' if it's a string. The input will be a single value that can be either an integer, float, or string.
"""

def variable_type(value):
    if isinstance(value, int):
        return 'integer'
    elif isinstance(value, float):
        return 'float'
    elif isinstance(value, str):
        return 'string'