"""
QUESTION:
Implement a function `product_of_list` that takes a list of numbers as input and returns the product of all numbers in the list. The function should have a time complexity of O(n), where n is the size of the list.
"""

from functools import reduce
from operator import mul

def product_of_list(lst: list):
    """
    Calculates the multiplication of all numbers in a list lst.
    """
    return reduce(mul, lst, 1)