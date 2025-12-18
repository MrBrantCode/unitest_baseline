"""
QUESTION:
Write a function `is_prime(n)` that checks if a given number `n` is prime, with a time complexity of O(sqrt(n)) and without using any built-in libraries or functions for prime number generation or factorization. The function should return `True` if the number is prime and `False` otherwise.
"""

import math

def is_prime(n):
    if n < 2:
        return False

    # Iterate from 2 to the square root of n (inclusive)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True