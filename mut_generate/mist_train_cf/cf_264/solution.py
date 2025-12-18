"""
QUESTION:
Create a function named `is_prime(n)` that determines whether a given integer `n` is prime or not. The function should have a time complexity of O(√n) and a space complexity of O(1).
"""

import math

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True