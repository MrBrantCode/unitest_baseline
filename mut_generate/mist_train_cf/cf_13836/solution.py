"""
QUESTION:
Write a function named `is_prime()` that determines whether a given number is prime or not. Using this function, compute the sum of all prime numbers within a specified range. The range is from 2 to 6 (inclusive) for this problem.
"""

def is_prime(n):
    """
    This function determines whether a given number is prime or not.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True