"""
QUESTION:
Create a function `check_prime(n)` that checks if a given number `n` is prime. The function should return `True` if the number is prime and `False` otherwise. The function should be optimized to only check divisibility up to the square root of `n` for efficiency. Use this function to print all odd prime numbers from 11 to 3000.
"""

import math

def check_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.sqrt(n)
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False
    return True