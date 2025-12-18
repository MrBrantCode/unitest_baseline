"""
QUESTION:
Create a function named `remove_all_duplicates` that takes a list `lst` and an element as input. The function should return a new list with all occurrences of the given element and its duplicates removed, preserving the original order of other elements in the list.
"""

def remove_all_duplicates(lst, element):
    return [x for x in lst if x != element]