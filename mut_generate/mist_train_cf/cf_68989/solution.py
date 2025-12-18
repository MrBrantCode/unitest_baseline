"""
QUESTION:
Write a function named `multiply_abs_values` that takes a list of numbers as input. The function should return the product of the integer parts of the absolute values of these numbers. The integer part of a number is the largest integer less than or equal to the number.
"""

import math

def multiply_abs_values(lst):
    product = 1
    for num in lst:
        product *= math.floor(abs(num))
    return product