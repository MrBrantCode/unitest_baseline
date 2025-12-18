"""
QUESTION:
Write a function `compute_sum(x, K)` that takes two parameters: a list `x` of up to 100 integers and a positive integer `K` less than or equal to 100. The function should return the sum of the elements in `x` with specific formatting. If the sum is divisible by `K`, it should be returned as a floating-point number with two decimal places of precision. Otherwise, the sum should be rounded up to the nearest integer value.
"""

import math

def compute_sum(x, K):
    total = sum(x)

    if total % K == 0:
        return format(total, ".2f")
    else:
        return math.ceil(total)