"""
QUESTION:
Create a function `is_prime` that takes an integer `num` as input and returns `True` if `num` is a prime number and `False` otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself. The function should be implemented using a lambda function in Python.
"""

def is_prime(num):
    """
    Checks if a number is a prime number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    return num > 1 and all(num%i != 0 for i in range(2, int(num**0.5) + 1))