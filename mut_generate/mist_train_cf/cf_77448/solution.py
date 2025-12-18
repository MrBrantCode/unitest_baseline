"""
QUESTION:
Write a function `odd_product(n, m)` that calculates the cumulative multiplication of all odd integers within a sequence of consecutive numbers from `n` to `m` (inclusive). The function should take two parameters `n` and `m`, where `n` and `m` are integers, and return the product of all odd integers in the specified range.
"""

def odd_product(n, m):
    product = 1
    for i in range(n, m + 1):
        if i % 2 != 0:
            product *= i
    return product