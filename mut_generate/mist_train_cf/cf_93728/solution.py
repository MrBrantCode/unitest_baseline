"""
QUESTION:
Create a function `add(a, b)` that takes two parameters, `a` and `b`. The function should return the sum of `a` and `b` with the following conditions: 
- If both `a` and `b` are integers, return the sum rounded to the nearest whole number.
- If either `a` or `b` is a floating-point number, return the sum rounded to two decimal places.
- If either `a` or `b` is `None`, return `None`.
- If either `a` or `b` is a string, list, or dictionary, return `None`.
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