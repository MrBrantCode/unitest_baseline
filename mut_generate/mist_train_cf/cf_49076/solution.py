"""
QUESTION:
Write a function named `count_equal_indices` that takes two lists of integers `lst1` and `lst2` as input and returns the count of indices where the lists have the same values, ignoring extra elements in the longer list and handling duplicate values.
"""

def count_equal_indices(lst1, lst2):
    return sum(1 for a, b in zip(lst1, lst2) if a == b)