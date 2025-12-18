"""
QUESTION:
Write a function `binomial_sum` that takes an integer `n` as input and returns the sum of the product of consecutive binomial coefficients. The function should use the `math.comb(n, k)` function from the math module to calculate the binomial coefficients. The product of consecutive binomial coefficients is defined as `math.comb(n, i) * math.comb(n, i+1)`, where `i` ranges from 0 to `n-2`.
"""

import math

def binomial_sum(n):
    total = 0
    for i in range(n-1):  
        total += math.comb(n, i) * math.comb(n, i+1)
    return total