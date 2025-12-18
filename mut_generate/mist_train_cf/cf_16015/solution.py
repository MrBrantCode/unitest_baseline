"""
QUESTION:
Create a 5x5 matrix and populate it with the first 25 prime numbers. Implement a function `is_prime(n)` that checks if a number `n` is prime. Use this function to validate the generated matrix. The `is_prime(n)` function should take an integer `n` as input and return a boolean indicating whether `n` is prime or not. The matrix should be a 2D list of integers, where each element is a prime number.
"""

import math

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
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True