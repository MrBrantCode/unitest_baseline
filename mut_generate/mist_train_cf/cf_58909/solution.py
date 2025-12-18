"""
QUESTION:
Design a function `is_perfect_square(n)` that determines if a given non-negative integer `n` is a perfect square. The function should return `True` if `n` is a perfect square and `False` otherwise. The input `n` is guaranteed to be a non-negative integer.
"""

import math

def entrance(n):
    square_root = math.sqrt(n)
    return square_root == int(square_root)