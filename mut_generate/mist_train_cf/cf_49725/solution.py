"""
QUESTION:
Create a function named `common_elements` that takes two lists, `list1` and `list2`, as input and returns a new list containing all elements that are common to both input lists.
"""

def common_elements(list1, list2):
    return [value for value in list1 if value in list2]