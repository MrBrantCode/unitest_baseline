"""
QUESTION:
Create a function `is_prime(n)` that checks whether a given number `n` is prime or not. The function should return `True` for prime numbers and `False` otherwise. The function should handle edge cases such as negative numbers and floating-point numbers. It should also be efficient for larger numbers, with a time complexity of at least O(sqrt(n)).
"""

import math

def is_prime(n):
    """Returns true for prime numbers, false otherwise."""
    if isinstance(n, (float, complex)) or n < 2: 
        return False
    for i in range(2, math.isqrt(n) + 1): 
        if n % i == 0:
            return False
    return True