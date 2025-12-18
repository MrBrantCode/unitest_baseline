"""
QUESTION:
Write a function named `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function should work efficiently for large numbers.
"""

def is_prime(n):
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True