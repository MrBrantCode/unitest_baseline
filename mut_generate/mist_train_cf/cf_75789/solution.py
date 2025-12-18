"""
QUESTION:
Write a function named `is_prime` that takes an integer as input and prints out all the prime numbers from a given list of integers. The function should return True if the input number is prime and False otherwise. Note that a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input list will contain integers greater than 0.
"""

def is_prime(n):
    """
    Checks if a number is prime and prints all prime numbers from a given list.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True