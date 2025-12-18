"""
QUESTION:
Create a function named `sum_of_squares_exclude_multiples_and_squares` that takes an integer `n` as input. The function should return the sum of the squares of all numbers from 1 to `n` (inclusive), excluding any multiples of 3 and perfect squares.
"""

import math

def sum_of_squares_exclude_multiples_and_squares(n):
    total = 0
    for i in range(1, n+1):
        if i % 3 != 0 and math.isqrt(i)**2 != i:
            total += i**2
    return total