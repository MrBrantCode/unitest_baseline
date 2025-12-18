"""
QUESTION:
Write a function `merge_arrays(arr1, arr2)` that merges two sorted arrays of integers into a single sorted array without using built-in functions for sorting. The resulting array should not contain any duplicate numbers. The function should have a linear time complexity of O(n+m) where n is the size of `arr1` and m is the size of `arr2`.
"""

def merge_arrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if arr1[i] not in result:
                result.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if arr2[j] not in result:
                result.append(arr2[j])
            j += 1
        else:
            if arr1[i] not in result:
                result.append(arr1[i])
            i += 1
            j += 1
    while i < len(arr1):
        if arr1[i] not in result:
            result.append(arr1[i])
        i += 1
    while j < len(arr2):
        if arr2[j] not in result:
            result.append(arr2[j])
        j += 1
    return result