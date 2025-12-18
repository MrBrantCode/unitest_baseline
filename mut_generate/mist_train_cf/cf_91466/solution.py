"""
QUESTION:
Create a function `mergeArrays(arr1, arr2)` that takes two sorted arrays `arr1` and `arr2` as input, merges them in ascending order while removing duplicates, and maintains the original order of the elements. The merged array should have no more than twice the length of the original arrays. The input arrays are guaranteed to be non-empty and contain only positive integers.
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