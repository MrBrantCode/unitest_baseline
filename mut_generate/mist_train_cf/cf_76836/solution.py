"""
QUESTION:
Create a function named `is_perfect_square` that takes a number `n` as input and returns `True` if `n` is a perfect square and `False` otherwise. The function should work with both positive and negative integers, but should return `False` for negative numbers since they cannot be perfect squares.
"""

import math

def is_perfect_square(n):
    if n < 0:
        return False
    root = math.sqrt(n)
    return n == int(root + 0.5) ** 2