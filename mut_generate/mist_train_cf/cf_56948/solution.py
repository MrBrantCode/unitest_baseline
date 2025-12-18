"""
QUESTION:
Write a function named `multiply_abs_values` that takes a list of numbers as input, rounds down each number to the nearest integer, calculates the absolute value of each rounded number, and returns the product of these absolute values. The function should return 0 if the list contains more than one zero (after rounding).
"""

import math

def multiply_abs_values(lst):
    product = 1
    zero_count = 0
    for i in lst:
        floored_value = math.floor(i)
        if floored_value == 0:
            zero_count += 1
            if zero_count > 1:
                return 0
        else:
            product *= abs(floored_value)
    return product