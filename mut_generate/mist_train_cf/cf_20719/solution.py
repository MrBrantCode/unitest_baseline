"""
QUESTION:
Write a function named `find_median` that calculates the median of a list of integers. The list will contain both positive and negative integers and have a length greater than 5. The function should return the calculated median.
"""

def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2