"""
QUESTION:
Implement a function named `mergeArrays` that takes two sorted arrays `arr1` and `arr2` as input, each containing only positive integers, and returns a new sorted array containing all unique elements from both arrays in ascending order while maintaining the original order of the elements. The input arrays are guaranteed to be non-empty, and the length of the merged array should be no more than twice the length of the original arrays.
"""

def mergeArrays(arr1, arr2):
    merged = []
    i, j = 0, 0

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

    return merged