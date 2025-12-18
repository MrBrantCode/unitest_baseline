"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns `True` if `n` is prime, and `False` otherwise. Using this function, write a code snippet to filter prime numbers from a given array of integers and calculate their sum. The function should consider a number `n` as prime if it is greater than 1 and has no divisors other than 1 and itself. The code should also handle the case where the input array is empty or contains non-prime numbers.
"""

def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True