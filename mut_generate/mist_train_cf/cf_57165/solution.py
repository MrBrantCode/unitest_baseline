"""
QUESTION:
Design a function `is_prime(n)` that checks if a given integer `n` is a prime number or not. The function should return `True` if the number is prime and `False` otherwise. The function should be efficient and should not check divisibility up to `n`, but up to its square root. The input number `n` will be between 1 and 1000.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True