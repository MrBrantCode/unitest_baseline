"""
QUESTION:
Write a function `find_median` that calculates the median of an array of floating point numbers. The function should handle both empty arrays and arrays containing negative numbers. The input array may have any number of elements, and the function should return the median as a floating point number. If the input array is empty, the function should return `None`.
"""

def find_median(nums):
    if len(nums) == 0: 
        return None
    sorted_nums = sorted(nums)
    mid = len(sorted_nums) // 2

    if len(sorted_nums) % 2 == 0:  # If even
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0
    else:  # If odd
        return sorted_nums[mid]