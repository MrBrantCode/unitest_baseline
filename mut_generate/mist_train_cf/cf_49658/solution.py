"""
QUESTION:
Write a function named `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. Use this function to generate a list of prime numbers within a given range, specifically from 15 to 30 (inclusive). The function should be able to handle numbers in the given range and should not include non-prime numbers in the output list.
"""

def entrance(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True