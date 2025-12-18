"""
QUESTION:
Develop the function `add_squared_values(lst)` that takes a list of numbers as input, rounds each number up to the nearest integer in its absolute form, squares the rounded numbers, and returns their sum.
"""

import math

def add_squared_values(lst):
    return sum(map(lambda x: math.ceil(abs(x)) ** 2, lst))