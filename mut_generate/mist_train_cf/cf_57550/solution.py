"""
QUESTION:
Write a function named `compare_lists` that compares two lists lexicographically. The function should take two lists as parameters and return a boolean value indicating whether the first list is less than the second list. The comparison should be done element-wise, and for nested lists, the comparison should also be done lexicographically.
"""

def compare_lists(list1, list2):
    if list1 < list2:
        return True
    else:
        return False