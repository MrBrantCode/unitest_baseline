"""
QUESTION:
Write a function `compute_sum(x, K)` that takes a list `x` of at most 100 integers and a positive integer `K` less than or equal to 100 as input. The function should compute the sum of the elements in `x` and check if the sum is divisible by `K`. If the sum is divisible by `K`, return the sum as a floating-point number with two decimal places of precision. Otherwise, return the sum rounded up to the nearest integer value. The function should have a time complexity of O(N), where N is the number of elements in `x`.
"""

import math

def compute_sum(x, K):
    total = sum(x)
    return "{:.2f}".format(total) if total % K == 0 else math.ceil(total)