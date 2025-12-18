"""
QUESTION:
Write a recursive function named `find_max` that takes a numeric array `arr` as input and returns the maximum value in the array. The array may contain negative numbers and will always have at least one element. The function should be efficient and able to handle large arrays.
"""

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    max_left = find_max(left_half)
    max_right = find_max(right_half)
    return max(max_left, max_right)