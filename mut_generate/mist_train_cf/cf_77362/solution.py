"""
QUESTION:
Write a function `common_elements(list1, list2)` that takes two lists of integers as input and returns a list of their common elements, keeping their order from the first list. The function should handle multiple instances of a number in the lists and include the minimum number of instances of each common element found in either list. The function should have a time complexity of O(n).
"""

from typing import List

def common_elements(list1: List[int], list2: List[int]) -> List[int]:
    dict1 = {}
    for i in list1:
        dict1[i] = dict1.get(i, 0) + 1
    dict2 = {}
    for i in list2:
        dict2[i] = dict2.get(i, 0) + 1

    result = []
    for num in dict1:
        if num in dict2:
            result.extend([num]*min(dict1[num], dict2[num]))
    return result