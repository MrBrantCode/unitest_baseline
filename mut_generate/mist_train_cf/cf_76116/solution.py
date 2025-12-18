"""
QUESTION:
Create a Python function `check_fibonacci` that takes a hexadecimal string as input and returns `True` if the decimal equivalent of the hexadecimal value has a Fibonacci sequence trait, and `False` otherwise. The function should use the property that a number is a Fibonacci number if either (5*n^2 + 4) or (5*n^2 - 4) is a perfect square. The input hexadecimal string should be in the format '0x...' and the function should support Python versions 3.8 and above.
"""

import math

def is_perfect_square(n):
    return n == math.isqrt(n) ** 2

def check_fibonacci(n):
    n_decimal = int(n, 16)  # converts from hexadecimal to decimal
    n1 = 5 * (n_decimal**2) + 4
    n2 = 5 * (n_decimal**2) - 4
    return is_perfect_square(n1) or is_perfect_square(n2)