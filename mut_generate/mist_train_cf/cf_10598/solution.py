"""
QUESTION:
Write a function named `find_median` that calculates the median of an array of integers, assuming the array length is an odd number. The function should return the median value and does not need to preserve the original order of the input array.
"""

def find_median(nums):
    nums.sort()  
    median_index = (len(nums) - 1) // 2  
    return nums[median_index]