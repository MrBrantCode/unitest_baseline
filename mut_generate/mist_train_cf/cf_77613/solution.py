"""
QUESTION:
Write a function `smallest_positive_missing_number(arr)` that takes an array of integers as input and returns the smallest positive integer that is not present in the array. The input array may contain negative numbers and non-contiguous integers. The function should handle these cases and return the smallest positive missing integer.
"""

def smallest_positive_missing_number(arr):
    arr = [i for i in arr if i > 0]
    if not arr:
        return 1
    arr.sort()
    smallest_positive_missing = 1
    for num in arr:
        if num == smallest_positive_missing:
            smallest_positive_missing += 1
        elif num > smallest_positive_missing:
            return smallest_positive_missing
    return smallest_positive_missing