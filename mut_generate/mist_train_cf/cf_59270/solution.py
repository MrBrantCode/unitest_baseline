"""
QUESTION:
Write a function `is_prime` that takes an integer `n` as input and returns a string indicating whether the number is "Prime", "Composite", or "Neither prime nor composite" if it's not a positive integer. The function must use the modulus operator to check for primality and should optimize performance by only checking divisibility up to the square root of `n`.
"""

import math

def is_prime(n):
    return "Neither prime nor composite" if n <= 1 else \
           "Composite" if any(n % i == 0 for i in range(2, math.isqrt(n) + 1)) else \
           "Prime"