"""
QUESTION:
Create a function named `symmetric_diff` that takes two lists `arr_1` and `arr_2` as input and returns a list of elements that are present in only one of the two lists, but not in both. The function should not consider duplicate values within each list. The input lists will contain distinct elements.
"""

def symmetric_diff(arr_1, arr_2):
    set_1 = set(arr_1)
    set_2 = set(arr_2)
    return list(set_1 ^ set_2)