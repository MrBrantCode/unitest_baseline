"""
QUESTION:
Write a function called `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. Use this function to generate a list of all prime numbers between 1 and 1000 inclusive. Note that the function should handle the case where `n` is less than 2.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True