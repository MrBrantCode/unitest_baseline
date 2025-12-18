"""
QUESTION:
Write a function `multiply_abs_values` that takes a list of numbers as input, calculates the product of their absolute values rounded down to the nearest integer, and returns the result.
"""

def multiply_abs_values(lst):
    result = 1
    for i in lst:
        result *= int(abs(i))
    return result