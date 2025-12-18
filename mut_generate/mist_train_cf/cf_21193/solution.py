"""
QUESTION:
Create a function named `is_prime(n)` that determines whether a given integer `n` is a prime number. The function should only consider input numbers between 2 and 10^9, inclusive, and must have a time complexity of O(sqrt(n)).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    
    return True