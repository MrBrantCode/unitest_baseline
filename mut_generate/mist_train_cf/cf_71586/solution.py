"""
QUESTION:
Create a function `is_prime` that takes an integer as input and returns `True` if the number is prime and `False` otherwise, given that the input number is between 1 and 30. The function should not take any other parameters.
"""

def is_prime(n):
    """
    Checks whether a number between 1 and 30 is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n > 1 and all(n % i for i in range(2, n)):
        return True
    else:
        return False