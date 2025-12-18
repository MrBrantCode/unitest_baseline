"""
QUESTION:
Write a function named `find_median` that takes an array of numbers as input, where the length of the array is an odd number. The function should return the median of the array, which is the middle value after the array is sorted in ascending order. The input array should contain at least one element.
"""

def find_median(nums):
    nums.sort()  # Sort the array in ascending order
    median_index = (len(nums) - 1) // 2  # Find the middle index
    return nums[median_index]  # Return the value at the middle index