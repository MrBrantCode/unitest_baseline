"""
QUESTION:
Create a function named `is_perfect_square` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a perfect square. The function should return `False` for negative numbers.
"""

import math

def is_perfect_square(n):
    if n < 0:
        return False
    root = math.sqrt(n)
    return int(root + 0.5) ** 2 == n