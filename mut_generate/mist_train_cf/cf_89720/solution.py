"""
QUESTION:
Write a function called `find_missing_number` that takes a list of integers as input and returns the missing number in a sequence of consecutive numbers starting from 1. The function should have a time complexity of O(n) and a space complexity of O(1), and it should not use any built-in Python functions or libraries (except for the len function).
"""

def find_missing_number(nums):
    n = len(nums) + 1  # Expected number of elements in the list
    expected_sum = (n * (n + 1)) // 2  # Sum of numbers from 1 to n
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number