"""
QUESTION:
Write a function named `is_prime` that checks if a number is prime or not and use it to calculate the sum of all prime numbers between 1 and 100.
"""

def is_prime(num):
    """
    Checks if a number is prime or not.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True