"""
QUESTION:
Create a function named `is_prime` that checks if a given number `n` is prime. Implement this function to find the first 100 prime numbers and calculate the sum of their cubes. The function `is_prime` should return `False` for numbers less than 2 and should not check for divisibility beyond the square root of `n`.
"""

def is_prime(n):
    """
    Checks if a given number n is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True