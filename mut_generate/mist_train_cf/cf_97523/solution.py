"""
QUESTION:
Write a function `compute_result` that takes two integers `a` and `b` as input, checks if their sum is odd, and if so, returns the square root of their product rounded to the nearest integer.
"""

import math

def compute_result(a, b):
    if (a + b) % 2 == 1:
        product = a * b
        result = round(math.sqrt(product))
        return result
    else:
        return None