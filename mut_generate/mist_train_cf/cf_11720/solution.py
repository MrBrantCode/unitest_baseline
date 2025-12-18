"""
QUESTION:
Write a function `compute_pi(n)` that calculates Pi to the nth digit using basic arithmetic operations and returns the result as a string. The function should only accept a positive integer for `n` and return an error message if `n` is not a positive integer.
"""

import math

def compute_pi(n):
    if not isinstance(n, int) or n < 1:
        return "Error: N must be a positive integer"
    
    return str(round(math.pi, n))