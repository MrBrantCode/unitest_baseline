"""
QUESTION:
Write a function `find_max(lst)` that returns the maximum element in a list `lst` without using the built-in `max()` function. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list. Do not use any loops or recursion in your solution.
"""

from functools import reduce

def entrance(lst):
    return reduce(lambda x, y: x if x > y else y, lst)