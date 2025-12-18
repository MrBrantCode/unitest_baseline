"""
QUESTION:
Implement a function named `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function should have a time complexity of O(sqrt(n)) and a space complexity of O(1).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # We only need to check divisibility up to the square root of n
    sqrt_n = int(math.sqrt(n)) + 1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True