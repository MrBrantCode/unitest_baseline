"""
QUESTION:
Create a function called `is_prime(n)` that determines whether a given number `n` is prime. The function should return `False` if `n` is not an integer or is less than or equal to 1. It should also return `False` if `n` has any divisors other than 1 and itself. The function should only consider integers and should handle cases where `n` is a decimal number.
"""

import math

def is_prime(n):
    # Check if n is a decimal or negative number
    if n != int(n) or n <= 1:
        return False
    
    # Check if n is divisible by any number from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True