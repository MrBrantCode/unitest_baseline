"""
QUESTION:
Implement a function `mergeSort(arr)` that recursively sorts an array of integers in O(n log n) time while removing any duplicate elements. The function should take an array `arr` as input and return the sorted array with no duplicates.
"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:  # Duplicate element found, skip it
            i += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result