"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given positive integer `n` is a prime number. The function should return `True` if `n` is prime and `False` otherwise. The time complexity of the function should be O(sqrt(n)).
"""

import math

def entrance(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True