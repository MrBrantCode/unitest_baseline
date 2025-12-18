"""
QUESTION:
Implement a function `compute_sum` that takes a list of integers as input and returns the sum of all the elements. You must use the `reduce()` function from the `functools` module and a lambda function to accumulate the sum. Do not use the built-in `sum()` function or any other functions that directly compute the sum. The function should have a time complexity of O(n), where n is the length of the input list.
"""

from functools import reduce

def compute_sum(lst):
    return reduce(lambda x, y: x + y, lst)