"""
QUESTION:
Generate a function `generateArray` that takes an array of two numbers as input. The function should calculate the maximum difference of 20% based on the larger number in the array and then return a new array where the larger number remains the same, but the smaller number is adjusted to be within the calculated 20% difference.
"""

def generateArray(nums):
    max_num = max(nums)
    min_num = min(nums)
    max_diff = max_num * 0.2
    adjusted_min_num = max_num - max_diff
    return [adjusted_min_num, max_num]