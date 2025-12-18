"""
QUESTION:
Determine if a given number is prime using a function called `is_prime` with a time complexity less than or equal to O(sqrt(n)). The function should take one integer `n` as input and return a boolean value indicating whether `n` is prime or not.
"""

import math

def is_prime(n):
    """
    Determine if a given number is prime with a time complexity of O(sqrt(n)).
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    
    # If n is less than 2, it's not prime
    if n < 2:
        return False
    
    # Check divisibility up to the square root of n
    for i in range(2, math.isqrt(n) + 1):
        # If n is divisible by i, it's not prime
        if n % i == 0:
            return False
    
    # If no divisors are found, n is prime
    return True