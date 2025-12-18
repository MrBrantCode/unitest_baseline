"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input, removes all duplicate characters while preserving the original order, and returns the resulting string. The function should be case-sensitive and should not affect the order of non-duplicate characters. Note that due to the immutability of Python strings, a space complexity of O(1) is not feasible; a solution with a space complexity of O(n) is acceptable.
"""

from collections import OrderedDict

def remove_duplicates(string): 
    return "".join(OrderedDict.fromkeys(string))