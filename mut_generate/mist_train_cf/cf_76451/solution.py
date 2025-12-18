"""
QUESTION:
Write a Python function `compute_geometric_mean(numbers)` that takes a list of 4 numbers as input and returns the geometric mean of these numbers. The geometric mean should be calculated by first finding the product of all the numbers, and then taking the fourth root of this product.
"""

import math

def compute_geometric_mean(numbers):
    # Compute the product of all the numbers
    product = math.prod(numbers)

    # Take the fourth root of the product
    return product ** 0.25