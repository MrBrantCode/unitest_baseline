"""
QUESTION:
Write a function `find_missing_number(arr)` that takes an array of n consecutive integers as input, where the array may contain duplicate numbers, and returns the missing number in the sequence. The function should not use any built-in functions or libraries.
"""

def find_missing_number(arr):
    n = len(arr)
    expected_sum = (n+1) * (n+2) // 2
    actual_sum = 0
    for num in arr:
        actual_sum += num
    missing_number = expected_sum - actual_sum
    return missing_number