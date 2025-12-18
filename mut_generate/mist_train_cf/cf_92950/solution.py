"""
QUESTION:
Design a function named `merge_sorted_arrays` that takes two sorted arrays of integers `arr1` and `arr2` as input and returns a new sorted array of size `n + m`, where `n` and `m` are the lengths of `arr1` and `arr2` respectively. The function should handle the cases where either array is empty, there are duplicate values, or there are negative numbers, and it should have a time complexity of O(n + m).
"""

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            merged.append(arr2[j])
            j += 1
        else:
            merged.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return sorted(list(set(merged)))