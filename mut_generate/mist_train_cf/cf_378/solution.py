"""
QUESTION:
Write a function `add(a, b)` that adds two numbers `a` and `b` and returns the result. The function should handle different types of inputs and return `None` for unsupported types. The function should return `None` when `a` or `b` is `None`, a string, a list, a dictionary, a tuple, a boolean, a set, or a complex number. When both `a` and `b` are integers, the function should return an integer result. For other numeric types, the function should return a floating-point number rounded to 2 decimal places.
"""

def add(a, b):
    if a is None or b is None:
        return None
    elif isinstance(a, (str, list, dict, tuple, bool, set, complex)) or isinstance(b, (str, list, dict, tuple, bool, set, complex)):
        return None
    elif isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return round(a + b, 2)