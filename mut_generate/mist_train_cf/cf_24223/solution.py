"""
QUESTION:
Write a function `compute_median` that calculates the median of a given list of integers. The list may be of any length and may contain both odd and even numbers of elements. The function should return the median value of the input list.
"""

def compute_median(nums):
    sorted_nums = sorted(nums)
    length = len(sorted_nums)
    mid = length // 2

    if length % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]