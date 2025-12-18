"""
QUESTION:
Write a function named `merge_sorted_arrays` that combines two sorted arrays `arr1` and `arr2` into one sorted array without using any built-in sorting functions or additional data structures. The function should achieve a time complexity of O(n), where n is the total number of elements in both `arr1` and `arr2`. The function should return the merged sorted array.
"""

def merge_sorted_arrays(arr1, arr2):
    pointer1 = 0
    pointer2 = 0
    merged = []

    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] <= arr2[pointer2]:
            merged.append(arr1[pointer1])
            pointer1 += 1
        else:
            merged.append(arr2[pointer2])
            pointer2 += 1

    while pointer1 < len(arr1):
        merged.append(arr1[pointer1])
        pointer1 += 1

    while pointer2 < len(arr2):
        merged.append(arr2[pointer2])
        pointer2 += 1

    return merged