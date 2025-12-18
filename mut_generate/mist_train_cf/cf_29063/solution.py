"""
QUESTION:
Write a function `find_first_zero_index` that takes a list of integer arrays as input and returns a list of integers representing the indices of the first occurrence of 0 in each array. If an array does not contain 0, the corresponding index in the returned list should be -1. The function should handle arrays of varying lengths and should return -1 for arrays where 0 is not present.
"""

from typing import List

def find_first_zero_index(arrays: List[List[int]]) -> List[int]:
    result = []
    for array in arrays:
        if 0 in array:
            result.append(array.index(0))
        else:
            result.append(-1)
    return result