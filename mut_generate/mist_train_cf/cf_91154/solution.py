"""
QUESTION:
Create a function `is_prime(n)` to check if a given number `n` is prime with a time complexity of O(sqrt(n)). The function should not use any built-in libraries or functions for prime number generation or factorization.
"""

import math

def entance(n):
    if n < 2:
        return False

    # Iterate from 2 to the square root of n (inclusive)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True