"""
QUESTION:
Write a function `is_prime` to check if a given number is prime or not. The function should take an integer as input and return True if the number is prime, False otherwise. The function should handle numbers less than or equal to 1 as non-prime numbers.
"""

def is_prime(num):
    """
    Checks if a given number is prime or not.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False