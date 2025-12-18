"""
QUESTION:
Write a function named `find_first_occurrence` that takes a list of integers with at least 3 elements and an integer element as input. The function should return the index of the first occurrence of the element in the list. If the element is not present in the list, the function should return -1. The function should use only basic array operations, without relying on any built-in functions or libraries.
"""

def find_first_occurrence(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1