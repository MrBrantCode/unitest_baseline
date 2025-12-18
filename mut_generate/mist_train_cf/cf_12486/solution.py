"""
QUESTION:
Write a function named `is_prime` and a main function to add a new prime number to the list `prime_numbers`. The `is_prime` function should take an integer `num` as input and return `True` if the number is prime, and `False` otherwise. The main function should append the next prime number after 5 to the list `prime_numbers` which initially contains the prime numbers [2, 3, 5].
"""

def is_prime(num):
    """
    Checks if a number is prime.
    
    Args:
    num (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True