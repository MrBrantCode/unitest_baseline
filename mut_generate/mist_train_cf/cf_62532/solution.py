"""
QUESTION:
Create a function `is_fibonacci(n)` that takes an integer `n` as input and returns `True` if `n` is a Fibonacci number, and `False` otherwise. A Fibonacci number is defined as a number that is a perfect square when either `(5*n^2 + 4)` or `(5*n^2 - 4)` is checked.
"""

import math

def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s*s == n
  
def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)