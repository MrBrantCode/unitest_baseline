"""
QUESTION:
Write a function named `evaluate_formula` that takes a single number `x` as input and returns the result of the mathematical expression `sqrt(x-3) + cos(2x)`. If `x-3` is negative, the function should return an error message. Assume that the `math` library is available for mathematical operations.
"""

import math

def evaluate_formula(x):
    if x-3 < 0:
        return "Error: Cannot take the square root of a negative number"
    else:
        return math.sqrt(x-3) + math.cos(2*x)