"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given number `n` is prime or composite with a time complexity of O(sqrt(n)). The function should return `True` if the number is prime and `False` otherwise.
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