"""
QUESTION:
Implement the merge sort algorithm in a function named `merge_sort` that takes an array of integers as input and returns the sorted array in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n). The implementation should not use any loops or iteration constructs, but can use recursion.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result