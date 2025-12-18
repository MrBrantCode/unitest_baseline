"""
QUESTION:
Create a function `is_prime(n)` that takes a positive integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function should only consider inputs within the range of 2 to 10^9, inclusive, and should have a time complexity of O(sqrt(n)).
"""

import math

def is_prime(n):
    # Check if number is within the valid range
    if n < 2 or n > 10**9:
        return False

    # Check divisibility from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True