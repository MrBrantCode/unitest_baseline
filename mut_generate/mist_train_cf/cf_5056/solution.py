"""
QUESTION:
Create a function `is_prime` that checks if an input value `n` is a prime number or not, returning `True` if prime and `False` otherwise. The function should have a time complexity of O(sqrt(n)) and a space complexity of O(1), without using any built-in functions or libraries for primality checks. The function should handle input values up to 10^9 and return the prime factorization and number of prime factors if the input value is not prime.
"""

import math

def is_prime(n):
    """
    Checks if an input value `n` is a prime number or not.
    
    Args:
    n (int): The input value to be checked.
    
    Returns:
    bool: True if `n` is prime, False otherwise.
    """
    
    # Check for base cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check for prime factors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True