"""
QUESTION:
Implement a function `binary_search(collection, start, end, value)` that takes a sorted collection of integers and the value to be found. The function should return the index of the value in the collection if it is present, and -1 if it is not found. The function should use binary search algorithm.
"""

from typing import List

def binary_search(collection: List[int], start: int, end: int, value: int) -> int:
    while start <= end:
        mid = start + (end - start) // 2
        if collection[mid] == value:
            return mid
        elif collection[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    return -1