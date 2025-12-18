"""
QUESTION:
Create a function `is_cubic_root_odd(num)` that takes a number `num` as input and returns `True` if the cubic root of `num` is an odd number and is a perfect cube, and `False` otherwise. The function should handle potential rounding issues with floating point arithmetic.
"""

import math

def is_cubic_root_odd(num):
    root = round(num ** (1. / 3))
    return root**3 == num and root % 2 == 1