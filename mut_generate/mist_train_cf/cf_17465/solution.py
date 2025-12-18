"""
QUESTION:
Implement a function `find_min_max(array: List[int]) -> Tuple[int, int]` that finds the maximum and minimum values in a given array of integers in a single traversal without using built-in functions or methods such as max() or min(). The function should return a tuple of the minimum and maximum values. The array may contain duplicate values and can be of any length. The function should have a time complexity of O(n). If the array is empty, the function should return None.
"""

from typing import List, Tuple

def find_min_max(array: List[int]) -> Tuple[int, int]:
    if len(array) == 0:
        return None

    min_val = array[0]
    max_val = array[0]

    for i in range(1, len(array)):
        if array[i] < min_val:
            min_val = array[i]
        elif array[i] > max_val:
            max_val = array[i]

    return (min_val, max_val)