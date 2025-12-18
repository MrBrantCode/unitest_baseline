"""
QUESTION:
Write a function called `merge_sorted_arrays` that takes two sorted arrays `arr1` and `arr2` as input. The function should return a new array that is a merged version of `arr1` and `arr2` in ascending order. The function should not use any additional memory or built-in functions for merging/sorting, and it should preserve the original arrays.
"""

def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    return merged