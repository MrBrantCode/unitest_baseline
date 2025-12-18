"""
QUESTION:
Write a function `is_evenly_divisible(x, y)` that takes two integers `x` and `y` as input and returns `True` if `x` is evenly divisible by `y`, and `False` otherwise. The function should assume that `y` is non-zero.
"""

def is_evenly_divisible(x, y):
    return x % y == 0