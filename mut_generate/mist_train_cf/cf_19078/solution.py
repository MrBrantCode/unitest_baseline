"""
QUESTION:
Write a function called `square_root_of_squared_element` that takes a list of numbers as input. The function should select the first element from the list, square it, and return the square root of the squared element rounded to the nearest whole number.
"""

import math

def entrance(lst):
    element = lst[0]
    squared = element**2
    square_root = math.sqrt(squared)
    return round(square_root)