"""
QUESTION:
Create a function called `is_prime(n)` that takes an integer `n` as input and returns a boolean indicating whether the number is prime. The function should handle numbers of any size, but optimization for large numbers is required. The function should return `False` for numbers less than or equal to 1, and it should check for divisibility up to the square root of `n` to optimize the process.
"""

import math

def is_prime(n):
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for x in range(3, sqrt_n + 1, 2):
        if n % x == 0:
            return False
    return True