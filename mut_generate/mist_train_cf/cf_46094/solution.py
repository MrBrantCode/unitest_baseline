"""
QUESTION:
Write a function `common_elements` that takes two lists of distinct integers as input and returns a list of integers that are common to both input lists, in the order they appear in the first list. The function must have a time complexity of O(n).
"""

from typing import List

def common_elements(list1: List[int], list2: List[int]) -> List[int]:
    set2 = set(list2) 
    return [value for value in list1 if value in set2]