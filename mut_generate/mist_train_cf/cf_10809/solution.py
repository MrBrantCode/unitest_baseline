"""
QUESTION:
Write a function `is_prime(n)` that checks if a number `n` is prime and use it to generate a list of all prime numbers in a given range from 1 to 100. The function should return `True` if the number is prime, and `False` otherwise. The prime-checking function should only consider divisors up to the square root of `n`.
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
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True