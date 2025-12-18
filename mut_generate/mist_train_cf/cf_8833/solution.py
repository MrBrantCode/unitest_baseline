"""
QUESTION:
Implement the function `calculate_sum()` that takes a list of numbers as a parameter, excludes any negative numbers from the sum, and returns the sum of the remaining numbers. The function should handle empty lists and have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1), i.e., it should not use any additional space proportional to the size of the input list.
"""

def calculate_sum(nums):
    return sum(num for num in nums if num >= 0)