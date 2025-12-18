"""
QUESTION:
Write a function `find_minimum_in_rotated_array(rotated: List[int]) -> int` that finds the minimum element in a rotated sorted array with no duplicate elements. The array is non-empty and formed by splitting a sorted array into two non-empty subarrays and reversing their order. Return the minimum element in the rotated array.
"""

from typing import List

def find_minimum_in_rotated_array(rotated: List[int]) -> int:
    left, right = 0, len(rotated) - 1

    while left < right:
        mid = left + (right - left) // 2

        if rotated[mid] > rotated[right]:
            left = mid + 1
        else:
            right = mid

    return rotated[left]