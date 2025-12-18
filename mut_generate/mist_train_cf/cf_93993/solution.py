"""
QUESTION:
Write a function named `find_second_minimum` that takes a list of integers as input and returns the second smallest element in the list. The list will contain at least two elements and may contain negative numbers and duplicates.
"""

def find_second_minimum(lst):
    return sorted(set(lst))[1]