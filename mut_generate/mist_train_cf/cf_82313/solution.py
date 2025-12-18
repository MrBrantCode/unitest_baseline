"""
QUESTION:
Create a function named `check_prime(n)` that determines if a given integer `n` is a prime number. The function should return `True` for prime numbers and `False` for non-prime numbers. Optimize the function to achieve a balance between space and time complexity. The function should handle integers of any value.
"""

import math

def check_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True