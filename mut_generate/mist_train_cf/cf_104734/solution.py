"""
QUESTION:
Write a function called `compute_median` that takes a list of integers as input and returns the median of the list. The function should not use any built-in functions or libraries to calculate the median. It should only use basic mathematical operations and loops.
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