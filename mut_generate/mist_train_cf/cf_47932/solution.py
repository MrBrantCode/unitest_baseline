"""
QUESTION:
Create a function named `common_elements` that takes two lists of integers, `list1` and `list2`, as input and returns a list of integers that are present in both lists, preserving their original order from `list1`. The lists contain no duplicate integers and the function should achieve an efficiency benchmark of O(n) time complexity.
"""

from typing import List

def common_elements(list1: List[int], list2: List[int]) -> List[int]:
    list2_elements = set(list2)
    return [el for el in list1 if el in list2_elements]