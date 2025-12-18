"""
QUESTION:
Write a function `find_second_minimum` that takes a list of numbers as input and returns the second smallest number in the list. The list will contain at least two elements and may include negative numbers and duplicates.
"""

def find_second_minimum(lst):
    lst.sort()
    return lst[1]