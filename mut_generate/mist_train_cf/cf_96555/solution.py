"""
QUESTION:
Find the missing number in an array of n consecutive integers, where the array may contain duplicate numbers, using the function `find_missing_number(arr)`, without using any built-in functions or libraries.
"""

def find_missing_number(arr):
    n = len(arr)
    expected_sum = (n+1) * (n+2) // 2
    actual_sum = 0
    for num in arr:
        actual_sum += num
    missing_number = expected_sum - actual_sum
    return missing_number