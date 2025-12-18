"""
QUESTION:
Write a function called `is_prime(N)` that checks if a given number `N` is a prime number. The function should return `True` if `N` is prime and `False` otherwise. The function must have a time complexity of O(sqrt(N)) and a space complexity of O(1), meaning it should not use any additional data structures.
"""

import math

def is_prime(N):
    # Check if N is less than 2
    if N < 2:
        return False

    # Iterate from 2 to the square root of N
    for i in range(2, int(math.sqrt(N)) + 1):
        # Check if i divides N evenly
        if N % i == 0:
            return False

    return True