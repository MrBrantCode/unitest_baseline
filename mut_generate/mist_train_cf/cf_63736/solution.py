"""
QUESTION:
Implement a function `shared_elements_extended` that takes three lists of integers as input and returns a list of distinct integers that are present in all three input lists, sorted in ascending order. The function should not use Python's built-in list functions for sorting, removing duplicates, or intersecting lists. The algorithm should have a time complexity of O(nlogn) or better.
"""

def shared_elements_extended(list1, list2, list3):
    dict1 = {}
    dict2 = {}
    dict3 = {}

    for i in list1:
        dict1[i] = 1
    for i in list2:
        if i in dict1:
            dict2[i] = 1
    for i in list3:
        if i in dict2:
            dict3[i] = 1

    result = list(dict3.keys())
    result.sort()

    return result