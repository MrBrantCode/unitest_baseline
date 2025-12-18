"""
QUESTION:
Write a function named `binomial_sum(n)` that calculates the sum of the product of consecutive binomial coefficients for a given range `n`. The function should handle edge cases where `n` is negative or zero. The function should return a meaningful error message if `n` is not a positive integer.
"""

import math

def binomial_sum(n):
    if not isinstance(n, int) or n < 0:
        return "Error: The input must be a positive integer!"

    result = 0

    if n == 0:
        return result

    for i in range(n):
        result += math.comb(n, i) * math.comb(n, min(i+1, n))
    return result