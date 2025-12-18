"""
QUESTION:
Implement a function `search` to find the index of a target value in a sorted array of distinct integers using a binary search algorithm. The function should take a list of integers `nums` and a target value `target` as input and return the index of the target if found, or -1 otherwise.
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1