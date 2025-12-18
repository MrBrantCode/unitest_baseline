"""
QUESTION:
Implement a function named `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. Use an efficient algorithm for checking primality.

You will be given a range of numbers as input from the user and you should find all prime numbers within that range and print them along with the total number of prime numbers found.
"""

import math

def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True