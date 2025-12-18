"""
QUESTION:
Write a function `is_perfect_square(n)` that checks if a given number `n` is a perfect square. The function should return `True` if `n` is a perfect square, and `False` otherwise. The function should be efficient and have a runtime complexity as close to constant time as possible.
"""

import math

def is_perfect_square(n):
    if n < 0:
        return False
    root = math.sqrt(n)
    return n == int(root + 0.5) ** 2