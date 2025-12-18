"""
QUESTION:
Create a function called is_prime(n) that takes a single integer n as input and returns True if the number is prime and False otherwise. The function should handle all positive integers and zero. The function should not be modified structurally, but its complexity can be increased to improve performance.
"""

from math import sqrt

def is_prime(n):
    """Returns true for prime integers, false for non-prime integers."""
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True