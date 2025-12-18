"""
QUESTION:
Create a function named `is_prime(n)` that determines whether a given integer `n` is prime or not. The function should be optimized to reduce its running time, and it should return a boolean value (`True` if `n` is prime, `False` otherwise). The function should only take an integer `n` as input and should not use any other parameters.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for x in range(3, int(math.sqrt(n)) + 1, 2):
            if n % x == 0:
                return False
    return True