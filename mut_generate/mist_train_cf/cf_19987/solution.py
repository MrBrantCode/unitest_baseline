"""
QUESTION:
Write a function `find_median` that takes a list of integers as input, where the list contains an odd number of elements. The function should return the median of the list. The time complexity of the function should be O(n log n).
"""

def find_median(nums):
    sorted_nums = sorted(nums)
    middle_index = len(sorted_nums) // 2
    return sorted_nums[middle_index]