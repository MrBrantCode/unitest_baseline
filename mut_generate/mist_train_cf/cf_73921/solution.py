"""
QUESTION:
Write a function `prime_number(n)` that checks if a given integer `n` is a prime number and returns a tuple. If `n` is a prime number, the function returns `(True, None)`. If `n` is not a prime number, the function returns `(False, divisor)`, where `divisor` is the smallest divisor of `n`. The function should be optimized to check for divisors only up to the square root of `n`. If `n` is less than 2, the function should return `(False, None)`.
"""

import math

def is_prime(n):
    if n < 2:
        return False, None
        
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False, i  # Return False and the divisor
            
    return True, None  # Return True if the number is prime