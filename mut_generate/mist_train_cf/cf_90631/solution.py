"""
QUESTION:
Write a function `max_difference(arr)` that takes an array of integers as input and returns the maximum difference between any two numbers in the array as an absolute value. The function should handle arrays of any length, including arrays with less than two elements. If the array has less than two elements, the function should return `None`.
"""

def max_difference(arr):
    if len(arr) < 2:
        return None

    min_num = arr[0]
    max_diff = 0

    for i in range(1, len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
        else:
            diff = arr[i] - min_num
            if diff > max_diff:
                max_diff = diff

    return max_diff