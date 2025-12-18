"""
QUESTION:
Create a function `is_strong_prime(n)` that checks whether a given number `n` is a strong prime number or not. A strong prime number is a prime number greater than 1, not a perfect square, and not a multiple of 2, 3, or 5. The function should return `True` if `n` is a strong prime, and `False` otherwise.
"""

import math

def is_strong_prime(n):
    # Check if n is greater than 1
    if n <= 1:
        return False
    
    # Check if n is a perfect square
    if math.isqrt(n) ** 2 == n:
        return False
    
    # Check if n is a multiple of the first three prime numbers
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    
    # Check if n is a prime number
    for i in range(7, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    
    return True