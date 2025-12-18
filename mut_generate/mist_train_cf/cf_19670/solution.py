"""
QUESTION:
Write a single-line function `ternary_operator` that takes an integer `x` and returns a value based on the following conditions: if `x` is less than 0, return -1; if `x` is equal to 0, return the value of `z` which is 2; if `x` is greater than 0, return the value of `z` which is 3.
"""

def ternary_operator(x, z):
    """Returns a value based on the given conditions."""
    return -1 if x < 0 else z if x == 0 else 3