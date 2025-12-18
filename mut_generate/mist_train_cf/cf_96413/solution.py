"""
QUESTION:
Write a function `compute_median` that takes a list of integers as input, sorts the list in ascending order, and returns the median without using any built-in functions or libraries for calculating the median. The function should handle both odd and even length lists by returning the middle element for odd lengths and the average of the two middle elements for even lengths.
"""

def compute_median(nums):
    # Step 1: Sort the list
    nums.sort()

    # Step 2: Check if the length is odd or even
    n = len(nums)
    if n % 2 == 0:
        # Length is even
        mid1 = nums[n // 2 - 1]
        mid2 = nums[n // 2]
        median = (mid1 + mid2) / 2
    else:
        # Length is odd
        median = nums[n // 2]
    
    return median