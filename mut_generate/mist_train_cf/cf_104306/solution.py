"""
QUESTION:
Write a function `find_outlier` that takes an array of integers as input and returns the integer that deviates from the mean of the array by the greatest margin. If there are multiple outlier values, return the smallest one.
"""

def find_outlier(nums):
    mean = sum(nums) / len(nums)
    max_deviation = max(abs(num - mean) for num in nums)
    return min(num for num in nums if abs(num - mean) == max_deviation)