"""
QUESTION:
Write a function named `merge_sorted_arrays` that takes two sorted arrays `arr1` and `arr2` as input, merges them into a single sorted array in descending order, removes duplicates while maintaining the relative order of elements, and limits the length of the merged array to at most twice the length of the original arrays. The input arrays are guaranteed to be non-empty.
"""

def merge_sorted_arrays(arr1, arr2):
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

    merged = list(set(merged))  # Removing duplicates
    merged.sort()  # Sorting in ascending order
    merged.reverse()  # Sorting in descending order

    return merged[:min(2*len(arr1), len(merged))]  # Limiting the merged array to have at most twice the length of the original arrays