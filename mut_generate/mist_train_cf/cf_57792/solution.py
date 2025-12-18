"""
QUESTION:
Write a function called `cumulative_product` that takes a single-dimension array of integers as input and returns the cumulative multiplication of all integer-based elements. The function should work for any array of integers, not just the example array [4, 6, 3, 9, 5].
"""

from functools import reduce

def cumulative_product(arr):
    return reduce((lambda x, y: x * y), arr)