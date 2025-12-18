"""
QUESTION:
Write a function `is_prime(n, start, end)` that checks if a given number `n` is prime within a given range from `start` to `end` (inclusive). The function should return `True` if `n` is prime within the range and `False` otherwise. The function should only consider numbers in the range for primality checks.
"""

def is_prime(n, start, end):
    for i in range(start, end + 1):
        if n % i == 0 and n != i and i != 1:
            return False
    return True