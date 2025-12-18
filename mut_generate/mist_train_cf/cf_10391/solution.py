"""
QUESTION:
Create a function named `calculate_median` that takes a list of numbers as input and returns the median of the list. The function should handle both even and odd lengths of input lists. The input list is not guaranteed to be sorted.
"""

def calculate_median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    return median