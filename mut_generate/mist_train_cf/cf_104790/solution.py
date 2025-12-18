"""
QUESTION:
Create a function named `is_prime` to determine if a given number is prime. Write a for loop that iterates through numbers from 1 to 100 and prints out the prime numbers using the `is_prime` function. The `is_prime` function should return `True` if the number is prime and `False` otherwise.
"""

def is_prime(num):
    """
    Check if a given number is prime.

    Args:
    num (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True