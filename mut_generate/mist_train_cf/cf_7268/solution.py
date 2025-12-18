"""
QUESTION:
Write a function called `is_prime` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number or not. The function should be able to handle large prime numbers efficiently and must be optimized for integers greater than 10^12. The function should return `True` if `n` is a prime number and `False` otherwise.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True