"""
QUESTION:
Write a function `find_common_elements` that takes two lists `list1` and `list2` as input parameters. The function should return a list of common elements from the two input lists, ignoring duplicates and in ascending order. The input lists can contain integers, floats, or strings, and can have a maximum length of 1000 elements.
"""

def find_common_elements(list1, list2):
    common_elements = list(set(list1) & set(list2))
    common_elements.sort()
    return common_elements