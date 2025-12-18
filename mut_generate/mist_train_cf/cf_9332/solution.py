"""
QUESTION:
Write a function `is_prime(N)` that checks if a given number `N` is prime. The function should return `True` if `N` is prime and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input `N` is a positive integer.
"""

import math

def is_prime(N):
    if N < 2:
        return False
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    
    return True