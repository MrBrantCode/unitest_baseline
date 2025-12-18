"""
QUESTION:
Write a function `sum_square_roots` that takes an array of integers as input and returns the sum of the square roots of the elements in the array that are perfect squares. If no element is a perfect square, return 0.
"""

import math

def sum_square_roots(arr):
    total = 0
    for num in arr:
        root = math.sqrt(num)
        if root.is_integer():
            total += root
    return total