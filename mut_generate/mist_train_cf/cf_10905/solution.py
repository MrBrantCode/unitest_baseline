"""
QUESTION:
Create a function called `is_prime` that determines whether a given number is a prime number or not. The function should take one argument, an integer `n`, and return `True` if `n` is a prime number, and `False` otherwise. The function should handle integers greater than 1.
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