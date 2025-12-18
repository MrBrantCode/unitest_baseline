"""
QUESTION:
Write a function `cubic_root_odd` that takes an integer as input and returns `True` if the number is a perfect cube and its cubic root is an odd integer, and `False` otherwise. The function should handle negative numbers by considering their absolute value and should return an error message if the input is not an integer.
"""

import math

def cubic_root_odd(value):
    try:
        value = int(value)
    except ValueError:
        return "Input must be an integer"
    else:
        if value < 0:
            value = abs(value)
        root = round(value ** (1/3))
        return root**3 == value and root % 2 != 0