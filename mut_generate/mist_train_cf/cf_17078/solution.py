"""
QUESTION:
Create a function named `calculate_median` that takes a list of numbers as input and returns the median of the list. The list may contain duplicates and negative numbers, and the function should handle both odd and even length lists.
"""

def calculate_median(nums):
    nums.sort()
    length = len(nums)
    if length % 2 != 0:
        median = nums[length // 2]
    else:
        median = (nums[length // 2 - 1] + nums[length // 2]) / 2
    return median