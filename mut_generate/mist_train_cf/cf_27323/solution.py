"""
QUESTION:
Write a function `searchInsert` that takes a sorted list of distinct integers `nums` and a target integer `target` as input, and returns the index where the target should be inserted in the list `nums` to maintain its sorted order. If the target is already present in the list, the function should return its index. If the target is not present in the list, the function should return the index where it would be if it were inserted. The input list `nums` is guaranteed to be non-empty.
"""

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left