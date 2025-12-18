"""
QUESTION:
Write a Python function named `aggregate_binomial(n)` that calculates the product of binomial coefficients from `n choose 2` to `n choose n` for a given positive integer `n` greater than 1, where `n choose k` is the binomial coefficient representing the number of ways to choose `k` items from `n` items without repetition and without order.
"""

import math

def aggregate_binomial(n):
    if n < 2:
        return "n should be greater than 1"
    res = 1
    for i in range(2, n+1):
        res *= math.comb(n, i)
    return res