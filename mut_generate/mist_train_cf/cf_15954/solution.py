"""
QUESTION:
Create a function `is_prime` to determine if a number is prime. The function should return a boolean value indicating whether the input number is prime or not, with the restriction that a prime number is a positive integer greater than 1 that is divisible only by itself and 1.
"""

def is_prime(num):
    """
    Checks if a number is prime.

    Args:
    num (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1