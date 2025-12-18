"""
QUESTION:
Create a function `calculate_median(nums)` that calculates the median of a given list of numbers. The list may contain duplicates and negative numbers. The function should return the median value. The input list is not guaranteed to be sorted.
"""

def calculate_median(nums):
    nums.sort()
    length = len(nums)
    if length % 2 != 0:
        median = nums[length // 2]
    else:
        median = (nums[length // 2 - 1] + nums[length // 2]) / 2
    return median