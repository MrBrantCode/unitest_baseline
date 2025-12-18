"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. Using this function, create a list of all prime numbers between 1 and 100. The list should include only integers that are greater than 1 and can only be divided evenly by 1 and themselves.
"""

def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True