"""
QUESTION:
Design a function `find_removal_point(lst, val)` that identifies the optimal rightmost point of removal for a specific value `val` in a sorted list `lst`, while maintaining the overall sorted sequence. The function should be able to handle lists containing various data types (integers, floats, strings, tuples, lists of lists) in both ascending and descending order, lists with duplicate values, and lists with mixed data types, including nested lists and tuples. If `val` is not found, the function should return -1.
"""

def find_removal_point(lst, val):
    for i in range(len(lst)-1, -1, -1):
        if type(lst[i]) in [list, tuple] and lst[i][-1] == val:
            return i
        if lst[i] == val:
            return i
    return -1