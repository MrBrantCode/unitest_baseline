"""
QUESTION:
Create a function called `is_prime` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a prime number or not. The function should efficiently handle large prime numbers (greater than 10^12). 

Restrictions: The input `n` is an integer.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True