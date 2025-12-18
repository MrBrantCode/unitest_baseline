"""
QUESTION:
Write a function `find_missing(lst)` that takes a list of integers as input, sorts it in ascending order, and returns a list of integers that are missing from the sorted list between the minimum and maximum values. The function should assume that the input list is a sequence with consecutive integers.
"""

def find_missing(lst):
    lst = sorted(lst)
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]