"""
QUESTION:
Write a function named `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise, with a time complexity of O(√m). Use this function to find the first 100 prime numbers and print them in reverse order.
"""

def is_prime(m):
    """
    Checks if a number is prime.

    Args:
    m (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if m < 2:
        return False
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True