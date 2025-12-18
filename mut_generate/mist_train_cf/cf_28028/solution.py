"""
QUESTION:
Write a function `checkPossibility(nums)` that determines if it's possible to make the array non-decreasing by modifying at most one element. The function should return `True` if it's possible to make the array non-decreasing by modifying at most one element, and `False` otherwise. The input is an array `nums` of integers.
"""

from typing import List

def checkPossibility(nums: List[int]) -> bool:
    cnt = 0  # Counter for the number of modifications
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            cnt += 1
            if cnt > 1:
                return False
            if i - 2 >= 0 and nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1]  # Modify the current element
            else:
                nums[i - 1] = nums[i]  # Modify the previous element
    return True