"""
QUESTION:
Write a function `is_prime(n)` that takes a positive integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function should not use any built-in libraries or functions for prime number calculation or checking, and it should have a time complexity of O(sqrt(n)).
"""

def is_prime(n):
    """
    Checks if a given positive integer is a prime number.
    
    Args:
        n (int): The number to be checked.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    return is_prime