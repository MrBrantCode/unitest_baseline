"""
QUESTION:
Write a function `is_multiple_of_seven_prime` that takes an integer `x` as input and returns a boolean value indicating whether `x` is a multiple of 7, is greater than or equal to 50, and is a prime number. Assume the existence of a helper function `isPrime(x)` to check if `x` is a prime number.
"""

def is_multiple_of_seven_prime(x, isPrime):
    """
    This function checks if a number is a multiple of 7, is greater than or equal to 50, and is a prime number.

    Args:
        x (int): The number to be checked.
        isPrime (function): A helper function to check if a number is prime.

    Returns:
        bool: True if the number is a multiple of 7, is greater than or equal to 50, and is a prime number; False otherwise.
    """

    return (x % 7 == 0) and (x >= 50) and isPrime(x)