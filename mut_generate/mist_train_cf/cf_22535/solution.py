"""
QUESTION:
Create a function merge_sorted_arrays(arr1, arr2) that merges two sorted arrays into a single sorted array with no duplicates. The merged array should be in non-decreasing order and the function should have a time complexity of O(n log n), where n is the total number of elements in both arrays.
"""

def merge_sorted_arrays(arr1, arr2):
    merged_arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            merged_arr.append(arr2[j])
            j += 1
        else:
            merged_arr.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    return merged_arr