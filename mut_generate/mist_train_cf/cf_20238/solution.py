"""
QUESTION:
Write a function `check_prime` that takes an integer `n` as input and returns a string stating whether the number is a prime number or not. The function should have a time complexity of O(sqrt(n)) and should not use any external libraries or functions to check for prime numbers, except for the math library to calculate the square root.
"""

import math

def check_prime(n):
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    str: A string stating whether the number is prime or not.
    """
    
    if n < 2:
        return f"{n} is not a prime number."
    
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return f"{n} is not a prime number."
    
    return f"{n} is a prime number."