"""
QUESTION:
Write a function named `is_prime` that takes an integer `n` as input and returns a boolean value indicating whether the number is prime or not. The function should have a time complexity of O(sqrt(n)).
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