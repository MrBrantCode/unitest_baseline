"""
QUESTION:
Write a function named `is_prime(n)` that checks if a given integer `n` is prime, with a time complexity of O(sqrt(n)). The function should return a boolean value indicating whether `n` is prime or not. The input `n` is a non-negative integer.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    
    is_prime = True
    sqrt_n = int(math.sqrt(n))
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            is_prime = False
            break
    
    return is_prime