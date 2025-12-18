"""
QUESTION:
Write a function `is_prime(N)` that checks if a given number `N` is prime. The function should return `True` if `N` is prime and `False` otherwise. The function must solve the problem in O(sqrt(N)) time complexity and use O(1) space complexity.
"""

import math

def entrance(N):
    # Check if N is less than 2
    if N < 2:
        return False

    # Iterate from 2 to the square root of N
    for i in range(2, int(math.sqrt(N)) + 1):
        # Check if i divides N evenly
        if N % i == 0:
            return False

    return True