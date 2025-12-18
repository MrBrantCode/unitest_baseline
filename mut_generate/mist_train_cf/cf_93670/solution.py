"""
QUESTION:
Create a function called `is_prime(n)` to determine whether a given number `n` is prime or not. The function should return `True` if `n` is prime and `False` otherwise. The function should handle all positive integers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for divisibility of n by numbers in the form of 6k ± 1 up to sqrt(n)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True