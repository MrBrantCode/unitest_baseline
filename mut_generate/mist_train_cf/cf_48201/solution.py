"""
QUESTION:
Implement a function named 'product_in_range' that takes in a list of integers 'l', an integer 'add_val', and a range defined by 'min_val' and 'max_val'. The function should return True if the sum of 'add_val' and the product of all elements in 'l' is within the range [min_val, max_val] (inclusive), and False otherwise. The time complexity of the function must be less than O(n^2).
"""

from functools import reduce
from operator import mul

def product_in_range(l: list, min_val: int, max_val: int, add_val: int) -> bool:
    """
    This function ascertains whether or not the added value of the product of every element in the list 'l' and 'add_val' is inside the range of 'min_val'(inclusive) and 'max_val' (inclusive).
    """
    product = reduce(mul, l, 1) 
    val = product + add_val 
    return min_val <= val <= max_val 