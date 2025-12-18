"""
QUESTION:
Create a function named `is_prime(n)` that determines whether a number `n` is prime or not, where `n` ranges from 2000 to 3200 (both included). The function should return `True` if `n` is divisible by both 7 and 13, but not a multiple of 5, and is a prime number; otherwise, return `False`.
"""

def is_prime(n):
    """
    Checks if a number n is prime.
    
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

def entrance(n):
    """
    Determines whether a number n is prime or not, 
    where n ranges from 2000 to 3200 (both included). 
    The function returns True if n is divisible by both 7 and 13, 
    but not a multiple of 5, and is a prime number; otherwise, return False.

    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if n meets the conditions, False otherwise.
    """
    if 2000 <= n <= 3200 and n % 7 == 0 and n % 13 == 0 and n % 5 != 0 and is_prime(n):
        return True
    return False