"""
QUESTION:
Construct a function `shared_elements(list1: list, list2: list)` that returns a list of unique elements common to both input lists, in ascending order. The function must not use Python's intrinsic list methods for sorting or removing duplicates, and it should have a time complexity of O(nlogn) or better.
"""

def shared_elements(list1: list, list2: list):
    dict1 = {i: True for i in list1}
    dict2 = {i: True for i in list2}
    output = sorted([item for item in dict1 if item in dict2])
    return output