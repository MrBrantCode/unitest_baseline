"""
QUESTION:
Write a function `find_missing_number` that takes an array of distinct integers in the range 0 to n, where n is the length of the array, and returns the missing number. The input array will always be non-empty and contain distinct numbers.
"""

def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)
    return expected_sum - actual_sum