"""
QUESTION:
Write a function named `find_missing_number` that takes a list of integers `arr` as input, representing n consecutive integers that may contain duplicates, and returns the missing number in the sequence. The length of the input list is n-1.
"""

def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number