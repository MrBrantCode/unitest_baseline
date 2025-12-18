"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given integer `n` is a prime number. The function should return `True` if `n` is prime and `False` otherwise. Your function should optimize the prime number check by only iterating up to the square root of `n` and handling the special case of even numbers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True