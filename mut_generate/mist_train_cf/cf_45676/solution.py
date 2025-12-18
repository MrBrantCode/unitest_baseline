"""
QUESTION:
Create a function named `is_prime(n)` that determines whether an integer `n` is prime or not. The function should handle edge cases and optimize the algorithm for efficiency. Implement the function to only check for divisibility up to the square root of `n` and avoid unnecessary checks for factors.
"""

import math
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3: 
        return True
    elif n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i = i + 6 
    return True