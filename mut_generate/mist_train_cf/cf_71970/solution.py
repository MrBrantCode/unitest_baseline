"""
QUESTION:
Write a function `find_max` that takes a list of integers as input and returns the maximum integer without using the built-in `max` function, sorting functions, or looping constructs like `for` or `while`. The function should be able to handle both positive and negative integers as well as zero, and it should work with lists of any length.
"""

from functools import reduce

def find_max(lst):
    return reduce((lambda x, y: x if (x>y) else y), lst)