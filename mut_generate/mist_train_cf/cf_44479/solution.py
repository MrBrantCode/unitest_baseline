"""
QUESTION:
Create a function named `is_unique_list` that takes a list of numbers as input and returns a boolean indicating whether all elements in the list are identical. The input list may be empty, in which case the function should return `False`.
"""

def is_unique_list(lst):
    return len(lst) > 0 and len(set(lst)) == 1