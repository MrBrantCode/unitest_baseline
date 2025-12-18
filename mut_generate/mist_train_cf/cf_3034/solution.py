"""
QUESTION:
Create a function `is_prime_and_divisible_by_seven` that checks if a given integer is a prime number greater than 100 and divisible by 7. The function should return `True` if the number meets these conditions, and `False` otherwise.
"""

import math

def is_prime_and_divisible_by_seven(value):
    # Check if value is greater than 100 and divisible by 7
    if value <= 100 or value % 7 != 0:
        return False
    
    # Check if value is a prime number
    for i in range(2, math.isqrt(value) + 1):
        if value % i == 0:
            return False
    return True