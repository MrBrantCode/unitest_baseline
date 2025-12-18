"""
QUESTION:
Create a function `is_prime_and_power_of_two(n)` that checks if a given positive integer `n` is both a prime number and a power of two. The function should return `True` if `n` satisfies both conditions and `False` otherwise. The input `n` is guaranteed to be a positive integer greater than or equal to 2.
"""

import math

def is_prime_and_power_of_two(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2

    return True