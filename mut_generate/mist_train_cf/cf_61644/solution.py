"""
QUESTION:
Design a function `is_fibonacci(n)` that takes a 32-bit signed integer `n` as input and returns "yes" if it is a Fibonacci number and "no" otherwise. The function should be able to handle any 32-bit integer and have a runtime complexity less than O(n).
"""

import math

def is_fibonacci(n):
    if n < 0:
        return "no"
    return 'yes' if is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4) else 'no'

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s*s == x