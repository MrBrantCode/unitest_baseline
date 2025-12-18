"""
QUESTION:
Implement a function named `check_prime(n)` that determines whether a given integer `n` is prime or not, returning `True` for prime integers and `False` otherwise. The function should optimize the primality check by only considering divisors up to the square root of `n`.
"""

import math

def check_prime(n):
    if n < 2:
        return False
    for number in range(2, math.isqrt(n) + 1):  
        if n % number == 0:
            return False
    return True