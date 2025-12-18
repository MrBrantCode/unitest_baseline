"""
QUESTION:
Write a function `find_median` that takes a list of integers as input and returns the median of the list. The list will always contain an odd number of elements. The function should have a time complexity of O(n log n).
"""

def find_median(nums):
    sorted_nums = sorted(nums)
    middle_index = len(sorted_nums) // 2
    return sorted_nums[middle_index]