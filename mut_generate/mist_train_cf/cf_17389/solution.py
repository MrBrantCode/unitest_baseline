"""
QUESTION:
Write a function `is_prime(n)` that checks if a number `n` is prime. Use this function to print all prime numbers between 0 and 100000 (inclusive). The function should be efficient and not check for divisibility beyond the square root of `n`.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True