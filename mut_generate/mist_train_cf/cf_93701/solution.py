"""
QUESTION:
Create a function named `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, or the smallest prime factor of `n` if it is not a prime number. The function should be able to handle inputs up to 10^9 and provide the result within 2 seconds.
"""

import math

def is_prime(n):
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