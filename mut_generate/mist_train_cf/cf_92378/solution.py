"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given integer `n` is a prime number. The function should return `True` if `n` is prime and `False` otherwise. The time complexity of the function should be O(sqrt(n)).
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    
    # Check if n is divisible by any number from 2 to sqrt(n)
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    
    return True