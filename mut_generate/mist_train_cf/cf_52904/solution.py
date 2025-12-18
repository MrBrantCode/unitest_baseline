"""
QUESTION:
Write a function called "merge_alternating" that takes in three lists of integers. The function should return a list where elements from the three input lists alternate. If one list is longer than another, the remaining elements of that longer list should be added at the end. The function should also handle the scenario where any of the lists might be empty.
"""

from typing import List
from itertools import zip_longest

def merge_alternating(list1: List[int], list2: List[int], list3: List[int]) -> List[int]:
    """
    Merge three input lists `list1`, `list2`, and `list3` by alternating their elements in the new list.
    """
    # This line does all the heavy lifting. Zip_longest merges the lists elementwise, returning None when 
    # it encounters the end of one list. The second 'for e' flattens the list out by iterating over the tuples
    # created by zip_longest.
    merged = [e for sublist in zip_longest(list1, list2, list3, fillvalue=None) for e in sublist if e is not None]
    return merged