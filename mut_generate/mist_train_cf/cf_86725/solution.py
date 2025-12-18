"""
QUESTION:
Write a function `find_max()` that takes an array of integers as input and returns a tuple containing the maximum number and its first occurrence index. The function should not use the built-in `max()` function and should have a time complexity of O(n log n). If the array contains duplicate numbers, the function should return the index of the first occurrence of the maximum number.
"""

def find_max(arr):
    if len(arr) == 1:
        return arr[0], 0

    mid = len(arr) // 2
    left_max, left_index = find_max(arr[:mid])
    right_max, right_index = find_max(arr[mid:])

    if left_max > right_max:
        return left_max, left_index
    elif right_max > left_max:
        return right_max, right_index + mid
    else:
        return left_max, left_index if left_index < right_index + mid else right_index + mid