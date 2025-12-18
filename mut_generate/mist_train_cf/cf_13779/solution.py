"""
QUESTION:
Design a function `merge_sorted_arrays` that takes two sorted arrays of integers, `arr1` and `arr2`, as input and returns a new sorted array containing all unique elements from both arrays. If either array is empty, return the non-empty array. The function should handle negative numbers and duplicate values correctly, and it should have a time complexity of O(n + m), where n and m are the lengths of `arr1` and `arr2`, respectively.
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