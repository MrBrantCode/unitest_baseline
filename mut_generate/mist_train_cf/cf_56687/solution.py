"""
QUESTION:
Create a function `advanced_negative_even_squares_sum` that takes a list of numbers as input. The function should return the cumulative product of the square roots of negative even integers in the list, ignoring positive or non-integer values. If the input list is empty or no negative even integers are found, the function should return 1.
"""

import math

def advanced_negative_even_squares_sum(lst):
    total = 1
    for el in lst:
        if isinstance(el, int) and el < 0 and el % 2 == 0:
            total *= math.sqrt(abs(el))
    return total