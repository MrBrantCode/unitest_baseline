"""
QUESTION:
Create a function `sum_nested_integers` that takes a 2D list as input, containing at least 3 nested lists with at least 3 integers each. The function should sum all integers in the list, ignore non-integer elements, and return the result rounded to the nearest whole number.
"""

import math

def sum_nested_integers(array):
    total_sum = 0
    for sublist in array:
        for element in sublist:
            if isinstance(element, int):
                total_sum += element
    return round(total_sum)