"""
QUESTION:
Write a function `distinct_product` that takes a list of integers as input, removes duplicates, and returns the product of the unique integers.
"""

from functools import reduce
import operator

def distinct_product(num_list):
    # Discern and isolate all distinct numerical entities in the series
    distinct_nums = set(num_list)
    
    # Calculate and manifest the multiplicative product of these unique units
    product = reduce(operator.mul, distinct_nums, 1)
    
    return product