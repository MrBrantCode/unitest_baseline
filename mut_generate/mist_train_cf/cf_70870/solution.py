"""
QUESTION:
Write a function named `IsPrime` that takes an integer `number` as input and returns `True` if the number is prime, `False` otherwise. The function should handle potential errors.
"""

def IsPrime(number):
    """
    Checks if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1: 
        return False
    if number == 2: 
        return True
    if number % 2 == 0: 
        return False

    boundary = int(number ** 0.5)

    # Check only odd numbers as even numbers are certainly not primes
    for i in range(3, boundary + 1, 2):
        if number % i == 0:
            return False

    return True