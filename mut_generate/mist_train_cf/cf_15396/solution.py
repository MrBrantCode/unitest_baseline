"""
QUESTION:
Create a function `is_prime(n)` that determines if a given input `n` is a prime number or not. If `n` is not a prime number, the function should return the smallest prime factor of `n`. The function should be able to handle inputs up to 10^9 and provide the result within 2 seconds. The function should return `True` if `n` is a prime number and the smallest prime factor if `n` is not a prime number.
"""

import math

def entrance(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return 2 if n % 2 == 0 else 3

    max_divisor = math.isqrt(n) + 1
    for divisor in range(5, max_divisor, 6):
        if n % divisor == 0:
            return divisor
        if n % (divisor + 2) == 0:
            return divisor + 2

    return True