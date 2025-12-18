"""
QUESTION:
Write a function `add(a, b)` that takes two arguments `a` and `b`. The function should add `a` and `b` and return the result. The function should handle the following requirements:
- The function should handle both integer and floating-point inputs for `a` and `b`.
- The function should return the result rounded to the nearest whole number if both `a` and `b` are integers.
- The function should return the result with two decimal places if either `a` or `b` is a floating-point number.
- The function should return `None` if `a` or `b` is `None`, a string, a list, or a dictionary.
"""

def add(a, b):
    if a is None or b is None:
        return None
    elif isinstance(a, (str, list, dict)) or isinstance(b, (str, list, dict)):
        return None
    elif isinstance(a, int) and isinstance(b, int):
        return round(a + b)
    else:
        return round(a + b, 2)