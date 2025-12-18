"""
QUESTION:
Write a Python function called `find_median` that takes a list of numbers as input and returns the median of the list. The function should handle both even and odd-length lists, and the input list is not guaranteed to be sorted.
"""

def find_median(nums):
    nums.sort()
    n = len(nums)
    
    if n % 2 == 0:
        median = (nums[n//2 - 1] + nums[n//2]) / 2
    else:
        median = nums[n//2]
        
    return median