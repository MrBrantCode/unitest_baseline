"""
QUESTION:
Write a function `is_prime` that checks if a given integer is prime or not. The function should take one integer parameter `n` and return a boolean value indicating whether the number is prime or not. Assume that the input `n` is a positive integer. The function should be efficient and not check for divisibility beyond the square root of `n`.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True