"""
QUESTION:
Write a function isPrime(x) that takes an integer x as input and returns a boolean indicating whether the number is a prime number between 1 and 100 exclusive. The function should return False for numbers less than or equal to 1, greater than or equal to 100, and non-prime numbers within the range.
"""

def is_prime(x):
    """
    Checks if a number is prime between 1 and 100 exclusive.

    Args:
        x (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if x <= 1 or x >= 100:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True