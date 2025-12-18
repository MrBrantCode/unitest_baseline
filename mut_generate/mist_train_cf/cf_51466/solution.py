"""
QUESTION:
Develop a function named `has_duplicates` that takes a list as input and returns a boolean value indicating whether the list contains any duplicate elements. The function should work for lists of any size and contain any type of elements.
"""

def has_duplicates(lst):
    return len(lst) != len(set(lst))