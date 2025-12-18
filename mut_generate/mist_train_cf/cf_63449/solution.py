"""
QUESTION:
Create a function `sqrt_sum_even(n)` that calculates the sum of all even numbers from 1 to `n`, and returns the square root of the sum, rounded down to the nearest integer. The function should be able to handle inputs up to `10^6`.
"""

import math

def sqrt_sum_even(n):
    n = n//2 
    total = n * (n + 1)
    return math.floor(math.sqrt(total))