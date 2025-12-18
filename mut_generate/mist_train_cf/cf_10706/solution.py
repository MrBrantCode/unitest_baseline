"""
QUESTION:
Write a function called `merge_sort_descending` that takes an array of integers as input and returns the array with its elements in descending order. The function should use the merge sort algorithm and have a time complexity of O(n log n).
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
    merged.extend(left if left else right)
    return merged