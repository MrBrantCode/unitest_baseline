"""
QUESTION:
Write a function `multiply_abs_values(lst)` that takes a list of numeric values, computes the absolute value of each number, converts these absolute values into their closest lower integers, and returns the product of these integers.
"""

import math

def multiply_abs_values(lst):
    product = 1
    for i in lst:
        product *= math.floor(abs(i))
    return product