"""
QUESTION:
Create a function `is_prime(n)` that checks if a given number `n` is a prime number with a time complexity of O(sqrt(n)). The function should return `True` if `n` is prime and `False` otherwise.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True