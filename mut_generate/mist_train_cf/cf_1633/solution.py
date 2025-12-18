"""
QUESTION:
Write a function called `find_median` that takes a list of integers as input and returns the median of the list. The function must handle lists with both positive and negative numbers and should not use built-in functions or libraries to calculate the median. The time complexity of the solution should be O(n log n), where n is the length of the list.
"""

def find_median(nums):
    nums.sort()  
    n = len(nums)
    if n % 2 == 0:  
        mid1 = nums[n//2]
        mid2 = nums[n//2 - 1]
        median = (mid1 + mid2) / 2
    else:  
        median = nums[n//2]
    return median