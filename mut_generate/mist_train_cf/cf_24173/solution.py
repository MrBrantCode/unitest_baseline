"""
QUESTION:
Write a function `isPrime(num)` that checks whether a given number is a prime number. The function should take an integer as input and return a boolean value indicating whether the number is prime or not. The input number is guaranteed to be a non-negative integer.
"""

def isPrime(num):
    """
    Checks whether a given number is a prime number.
    
    Args:
    num (int): The input number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    
    # Edge cases:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True