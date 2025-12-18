"""
QUESTION:
Create a function called `are_equal` that takes two numerical parameters, `a` and `b`, and returns `True` if they are equal and `False` otherwise. You cannot use any comparison operators (==, !=, <, >) or built-in functions (e.g., equals(), compareTo()) to compare the values. The function should work for any numerical values, but it does not need to handle NaN (Not a Number) or infinity.
"""

def are_equal(a, b):
    diff = a - b
    return diff == 0