"""
QUESTION:
Write a function `is_prime(n)` that determines whether a given number `n` is prime or not. The function should return a boolean value. Optimize the code to have the lowest possible time complexity. Note that `n` can be any non-negative integer.
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