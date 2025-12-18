"""
QUESTION:
Create a function named `find_median` that takes a list of integers as input, sorts the list in ascending order, and returns the median value of the list. The function should handle both even and odd length lists, where the median of an even length list is the average of the two middle numbers.
"""

def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:  
        return nums[n // 2]
    else:  
        return (nums[n // 2 - 1] + nums[n // 2]) / 2