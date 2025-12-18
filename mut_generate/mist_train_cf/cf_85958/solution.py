"""
QUESTION:
Write a function `is_prime` that takes an integer `number` as input and returns `True` if the number is prime and `False` otherwise. A prime number has only two distinct positive divisors: 1 and the number itself. The function should be able to handle numbers in the range from 1 to 100.
"""

def is_prime(number):
    """
    Checks if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True