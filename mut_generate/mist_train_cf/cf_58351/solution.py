"""
QUESTION:
Implement the function `is_prime` that checks whether a given number is prime or not. The function should return `True` if the number is prime, and `False` otherwise.
"""

def is_prime(n):
    """
    Checks whether a given number is prime or not.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True