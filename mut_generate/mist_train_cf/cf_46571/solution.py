"""
QUESTION:
Create a function `is_prime` that checks if a given number is prime. Use this function in a loop to find and print all prime numbers between 20 and 40 (inclusive). The function should return a boolean value indicating whether the number is prime or not.
"""

def is_prime(n):
    """
    Checks if a given number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True