"""
QUESTION:
Create a function named `mergeSort` that takes an array of integers as input. The function should return a new array containing the same integers, sorted in ascending order. The implementation must have a time complexity of O(nlogn) and use only constant extra space. The function should not use any built-in sorting functions or data structures. The input array can be of any length and may contain duplicate values, but the solution provided uses an array with 10 distinct integers from 0 to 9.
"""

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged