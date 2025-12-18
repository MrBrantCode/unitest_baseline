"""
QUESTION:
Construct a function `cumulative_product_nCr(n)` that calculates the cumulative product of consecutive binomial coefficients `math.comb(n, i)` for `i` in the range from 0 to `n-1`. The function should return a meaningful error message if the input `n` is not a positive integer.
"""

import math

def cumulative_product_nCr(n):
    if type(n) != int or n < 1:
        return "Error: Input should be a positive integer."

    product = 1
    for i in range(n):
        product *= math.comb(n, i)
      
    return product