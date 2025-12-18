"""
QUESTION:
Write a function `merge_sort` that takes a list of integers as input, sorts it in ascending order, and returns the sorted list. The function should have a time complexity of O(n log n).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    while left:
        merged.append(left.pop(0))
    while right:
        merged.append(right.pop(0))

    return merged