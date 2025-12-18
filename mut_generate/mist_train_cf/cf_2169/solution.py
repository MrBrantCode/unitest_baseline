"""
QUESTION:
Create a function `calculate_median(nums)` that takes a list of numbers as input, which may contain duplicates and negative numbers, and returns the median of the list. The function should have a time complexity of O(nlogn) and a space complexity of O(1).
"""

def calculate_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:  
        mid1 = n // 2
        mid2 = mid1 - 1
        return (nums[mid1] + nums[mid2]) / 2
    else:  
        mid = n // 2
        return nums[mid]