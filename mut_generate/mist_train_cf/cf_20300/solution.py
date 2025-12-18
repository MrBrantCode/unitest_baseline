"""
QUESTION:
Find the number of occurrences of a target element in an array of integers and return a sorted list of its indices. 

The input array can contain up to 1 million elements, including both positive and negative integers. The target element can be any integer value. The solution must have a time complexity of O(n) or better. Implement the function `findOccurrences(array: List[int], target: int) -> List[int]`.
"""

from typing import List

def findOccurrences(array: List[int], target: int) -> List[int]:
    return [i for i, num in enumerate(array) if num == target]