"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number. If `n` is not a prime number, the function should return the smallest prime factor of `n`. The function should be able to handle integers greater than 1.
"""

import math

def entance(n):
    # Check if n is less than 2 (not a prime number)
    if n < 2:
        return False
    
    # Check for factors from 2 to square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        # If n is divisible by i, it's not a prime number
        if n % i == 0:
            return i
    
    # If no factors found, it's a prime number
    return True