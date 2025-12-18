"""
QUESTION:
Write a function `compute_product(arr)` that takes an array of numbers as input and returns the product of the elements that are multiples of both 3 and 5, excluding elements equal to 2 or 3, and rounded to the nearest integer.
"""

import math

def compute_product(arr):
    product = 1

    for num in arr:
        if num % 3 == 0 and num % 5 == 0 and num != 2 and num != 3:
            product *= num

    product = round(product)

    return product