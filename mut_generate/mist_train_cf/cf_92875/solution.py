"""
QUESTION:
Write a function named `find_missing_number` that takes an array of n consecutive integers as input, where the array may contain duplicate numbers. The function should return the missing number in the array. The input array will have a length of n-1, where n is the number of consecutive integers in the complete sequence.
"""

def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number