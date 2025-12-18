"""
QUESTION:
Write a function `is_prime(n)` that takes a positive integer `n` and returns `True` if it is a prime number, and `False` otherwise. A prime number is defined as a number greater than 1 that has no positive divisors other than 1 and itself.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True