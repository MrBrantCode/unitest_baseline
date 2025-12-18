"""
QUESTION:
Create a function called `is_perfect_square` that takes a single integer `n` as input and returns a boolean indicating whether the number is a perfect square. The function should use the `math` module and work for positive integers.
"""

import math

def is_perfect_square(n):
    return math.isqrt(n)**2 == n