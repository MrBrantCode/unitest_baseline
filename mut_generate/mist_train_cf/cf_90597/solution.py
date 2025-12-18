"""
QUESTION:
Implement the function `calculate_sum()` that takes in a list of numbers as a parameter and returns the sum of non-negative numbers in the list. The function should handle empty lists as well. The function should use a recursive approach to calculate the sum and have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1).
"""

def calculate_sum(nums):
    if not nums:
        return 0
    if nums[0] < 0:
        return calculate_sum(nums[1:])
    return nums[0] + calculate_sum(nums[1:])