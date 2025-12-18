"""
QUESTION:
Design a function called `is_prime_palindromic` that takes an integer `n` as input and returns `True` if the number is both prime and palindromic, and `False` otherwise. The function should be able to check all numbers between 1 and 100.
"""

def is_prime_palindromic(n):
    """
    Checks whether a number is both prime and palindromic.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is both prime and palindromic, False otherwise.
    """
    
    # Function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Function to check if a number is palindromic
    def is_palindromic(num):
        return str(num) == str(num)[::-1]
    
    return is_prime(n) and is_palindromic(n)