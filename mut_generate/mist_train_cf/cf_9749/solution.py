"""
QUESTION:
Implement a function named `merge_sort` that takes a list of integers as input and returns the sorted list using the Merge Sort algorithm. The `merge_sort` function should call a helper function named `merge` to merge two sorted sublists. The input list can contain duplicate values and the output should be in ascending order. The list should be sorted in-place, without using any built-in sorting functions.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged