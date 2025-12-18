"""
QUESTION:
Create a function `calculate_median` that calculates the median of a set of numbers. The function should take a list of integers as input, including potential duplicates and negative numbers. The function must have a time complexity of O(nlogn) and a space complexity of O(1). The function should return the calculated median.
"""

def calculate_median(nums):
    nums.sort()  # Sort the set in ascending order

    n = len(nums)
    if n % 2 == 0:  # Even length
        mid1 = n // 2
        mid2 = mid1 - 1
        return (nums[mid1] + nums[mid2]) / 2
    else:  # Odd length
        mid = n // 2
        return nums[mid]