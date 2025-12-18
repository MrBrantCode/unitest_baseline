"""
QUESTION:
Create a function `add(a, b)` that takes two parameters `a` and `b` and returns their sum. The function should only accept positive integers as input and return an error message if either `a` or `b` is not a positive integer.
"""

def add(a, b):
    if isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0:
        return a + b
    else:
        return "Error: both a and b need to be positive integers."