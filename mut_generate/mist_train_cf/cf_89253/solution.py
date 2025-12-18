"""
QUESTION:
Write a function `find_max(lst)` that takes a list of integers as input and returns the maximum element in the list. The function should not use the built-in `max()` function, loops, or recursion. The time complexity should be O(n) and the space complexity should be O(1).
"""

from functools import reduce

def find_max(lst):
    return reduce(lambda x, y: x if x > y else y, lst)