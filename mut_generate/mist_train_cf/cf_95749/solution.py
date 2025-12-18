"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given positive integer `n` is a prime number. The function should return `True` if the number is prime and `False` otherwise, and it should have a time complexity of O(sqrt(n)).
"""

import math

def entrance(n):
    # Check if n is less than 2
    if n < 2:
        return False

    # Iterate from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        # Check if i evenly divides n
        if n % i == 0:
            return False

    # If no number evenly divides n, it is prime
    return True