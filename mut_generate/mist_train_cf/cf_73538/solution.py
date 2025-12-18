"""
QUESTION:
Write a function `is_less(list1, list2)` that takes two lists of integers as input and returns `True` if all elements in `list1` are less than their corresponding elements in `list2`, and `False` otherwise. Assume that the input lists are of the same length.
"""

def is_less(list1, list2):
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False
    return True