"""
QUESTION:
Implement the function `findOccurrences(array: List[int], target: int) -> List[int]` that finds the number of times a given target element appears in the array and returns a list of indices where the target element is found, sorted in ascending order. The array can contain up to 10 million elements and can have both positive and negative integers. The time complexity of the solution should be O(n) or better.
"""

from typing import List

def findOccurrences(array: List[int], target: int) -> List[int]:
    indices = []
    for i in range(len(array)):
        if array[i] == target:
            indices.append(i)
    return indices