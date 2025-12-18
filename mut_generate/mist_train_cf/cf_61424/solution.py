"""
QUESTION:
Create a function `is_prime` that determines whether a given integer is prime or composite and returns 'Prime' or 'Composite' accordingly. The input is a single integer. The function should only check divisibility up to the square root of the number.
"""

import math

def entrance(num):
    if num < 2:
        return 'Composite'
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return 'Composite'
    return 'Prime'