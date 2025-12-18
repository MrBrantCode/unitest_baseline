"""
QUESTION:
Given an array of integers and a target element, implement the function `findOccurrences(array: List[int], target: int) -> List[int]` to find the indices at which the target element occurs in the array. The function should return a list of indices in ascending order and have a time complexity of O(n) or better. The array can contain up to 10 million elements and the target element can be any integer value.
"""

from typing import List

def entrance(array: List[int], target: int) -> List[int]:
    indices = []
    for i in range(len(array)):
        if array[i] == target:
            indices.append(i)
    return indices