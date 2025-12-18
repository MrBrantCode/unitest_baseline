"""
QUESTION:
Implement a `merge_sort` function that takes an array of integers as input and returns the array sorted in ascending order. The function should be a recursive implementation of the merge sort algorithm.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left[0])
            left = left[1:]
        else:
            merged.append(right[0])
            right = right[1:]

    while left:
        merged.append(left[0])
        left = left[1:]

    while right:
        merged.append(right[0])
        right = right[1:]
    return merged