"""
QUESTION:
Create a function `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function should handle integers of any size, but it is optimized for performance by only checking divisibility up to the square root of `n`.
"""

import math

def is_prime(n):
    if n == 2: 
      return True
    elif n < 2 or n % 2 == 0: 
      return False
    for current in range(3, int(math.sqrt(n)) + 1, 2):
        if n % current == 0:
            return False
    return True