"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function should handle the case when `n` is less than or equal to 1.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True