"""
QUESTION:
Implement a function named `sort_array` that takes an array of integers as input and returns the array sorted in ascending order. The function must have a time complexity of O(n log n) and cannot use any built-in sorting functions or methods. The array can contain both positive and negative integers, and the function should handle duplicate elements efficiently. The implementation should use a divide and conquer algorithm such as merge sort or quicksort.
"""

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort_array(arr[:mid])
    right = sort_array(arr[mid:])
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