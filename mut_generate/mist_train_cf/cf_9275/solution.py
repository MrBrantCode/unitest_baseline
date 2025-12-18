"""
QUESTION:
Create a function called merge_sort_descending that implements the merge sort algorithm to sort an array of integers in descending order. The function should take an array of integers as input and return the sorted array.
"""

def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort_descending(arr[:mid])
    right_half = merge_sort_descending(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    while left and right:
        if left[0] > right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged