"""
QUESTION:
Create a function called `is_prime` that determines whether a given number `n` is prime, with the following conditions: 

- The time complexity of the algorithm should be below O(n).
- The function should handle cases up to 10^12.
- The input `n` is an integer. 

The function should return a boolean value indicating whether the number is prime or not.
"""

import math

def is_prime(n):
    """Check if the number n is prime"""
    if n <= 1: 
        return False
    if n == 2: 
        return True
    # Check from 2 to the sqrt of n
    for number in range(2, math.isqrt(n) + 1):
        if n % number == 0: 
            return False
    return True