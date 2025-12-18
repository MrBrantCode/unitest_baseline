"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` and returns `True` if `n` is prime, and `False` otherwise. The function should handle integers of all sizes, but can assume that the input will always be an integer.
"""

def is_prime(n):
    """Return True if given number is prime, False otherwise."""
    
    # All integers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisibility by integers from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    # If no divisor found, the number is prime
    return True