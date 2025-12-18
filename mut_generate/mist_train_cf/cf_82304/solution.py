"""
QUESTION:
Construct a function `perfect_squares` that takes a list of integers as input and returns a new list containing only the perfect squares from the original list using list comprehension. The function should not take any other arguments besides the list of integers.
"""

import math

def perfect_squares(lst):
    """Returns a new list containing only the perfect squares from the original list."""
    return [num for num in lst if math.sqrt(num).is_integer()]