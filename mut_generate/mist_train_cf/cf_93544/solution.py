"""
QUESTION:
Write a function named `is_prime(n)` that determines if a given integer `n` is prime or composite with a time complexity of O(sqrt(n)). The function should return `True` if `n` is prime, and `False` otherwise. The function must handle edge cases, including numbers less than or equal to 1.
"""

import math

def is_prime(n):
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check divisibility up to square root of n
    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False

    return True