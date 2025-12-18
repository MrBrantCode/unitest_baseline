"""
QUESTION:
Write a function `complex_computation(lst)` that takes a list of numeric values as input, computes the absolute value of each number, converts these absolute values to their closest lower integers, arranges the integers in increasing order, and returns the product of these integers excluding the smallest two numbers. If the list has two or fewer elements, return 0.
"""

from math import floor
from functools import reduce

def complex_computation(lst):
    # converting each number to its absolute value and then to lower integer
    lst = [floor(abs(i)) for i in lst]

    # sorting the list
    lst.sort()

    # Multiplying all elements except the smallest two
    product = reduce(lambda x, y: x * y, lst[2:]) if len(lst) > 2 else 0
    
    return product