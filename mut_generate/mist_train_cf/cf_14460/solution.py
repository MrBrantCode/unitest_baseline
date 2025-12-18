"""
QUESTION:
Write a function named `is_prime(n)` that checks if a given number `n` is prime. The function should have a time complexity of O(sqrt(n)) and return a boolean value indicating whether `n` is prime or not.
"""

import math

def entrance(n):
    if n < 2:
        return False
    
    is_prime = True
    sqrt_n = int(math.sqrt(n))
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            is_prime = False
            break
    
    return is_prime