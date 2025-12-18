"""
QUESTION:
Write a function `find_min_max` that takes an array of integers as input and returns a tuple containing the minimum and maximum values in the array. The array can be of any length between 1 and 10^6, can have duplicate values, and is not guaranteed to be sorted.
"""

def find_min_max(nums):
    if not nums:
        return None
    
    min_val = max_val = nums[0]
    for num in nums[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return (min_val, max_val)