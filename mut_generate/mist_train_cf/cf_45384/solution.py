"""
QUESTION:
Create a function `multiply_abs_values` that takes a list of numbers as input. The function should return the product of the maximum integer less than or equal to the absolute value of each number in the list.
"""

import math

def multiply_abs_values(lst):
    result = 1
    for number in lst:
        result *= math.floor(abs(number))
    return result