"""
QUESTION:
Write a function named `is_prime` that takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. The function should be able to efficiently check for primality for numbers up to 1,000,000,000.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True