"""
QUESTION:
Create a function named `cumulative_binomial_product` that calculates the cumulative sum of the product outcomes of consecutive binomial coefficients. The function should take an integer `n` as input, iterate from `1` to `n-1`, and return the sum of the products of `comb(n, i)` and `comb(n, i + 1)` for each `i` in the range.
"""

from math import comb

def cumulative_binomial_product(n):
    cumulative_sum = 0
    for i in range(1, n):
        cumulative_sum += comb(n, i) * comb(n, i + 1)
    return cumulative_sum