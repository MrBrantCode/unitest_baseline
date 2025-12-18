"""
QUESTION:
Write a function `is_prime(n)` that checks if a number `n` is prime. The function should be optimized for efficiency, and it should only return a boolean value indicating whether the number is prime or not. The input `n` will be a positive integer.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True