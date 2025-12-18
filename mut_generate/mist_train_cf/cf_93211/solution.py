"""
QUESTION:
Write a function named `is_prime` that takes a positive integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. A prime number is defined as a number greater than 1 that has no positive divisors other than 1 and itself. The function should be efficient and should not check for divisors beyond the square root of `n`.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True