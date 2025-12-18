"""
QUESTION:
Find the number of occurrences of a target element in an array of integers and return a list of indices where the target element is found, sorted in ascending order. The function `findOccurrences(array: List[int], target: int) -> List[int]` should have a time complexity of O(n) or better, where n is the length of the array. The array can contain up to 1 million elements and can include both positive and negative integers.
"""

from typing import List

def findOccurrences(array: List[int], target: int) -> List[int]:
    indices = [i for i, num in enumerate(array) if num == target]
    return indices