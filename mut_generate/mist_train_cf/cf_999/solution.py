"""
QUESTION:
Write a function `find_max(arr)` that finds the maximum number in an array without using the built-in `max()` function and returns the maximum value along with its index. The function should have a time complexity of O(n log n) and handle cases with duplicate numbers by returning the index of the first occurrence of the maximum number.
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