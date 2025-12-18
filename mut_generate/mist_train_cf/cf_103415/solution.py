"""
QUESTION:
Create a Python function named `is_prime_number` that takes an integer as input and returns a boolean value indicating whether the number is prime or not. The function should be able to handle numbers up to 50. Implement this function and use it to print all prime numbers up to 50.
"""

def is_prime_number(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True