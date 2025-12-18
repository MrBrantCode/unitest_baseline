"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function should have a time complexity of O(sqrt(n)).
"""

import math

def entrance(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True