"""
QUESTION:
Write a function `merge_arrays` that merges two sorted arrays `arr1` and `arr2` in descending order. The function should take two lists of integers as input, where each list is sorted in descending order. The function should return a new list containing all elements from both input lists, sorted in descending order.
"""

def merge_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] >= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append the remaining elements of arr1, if any
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    # Append the remaining elements of arr2, if any
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged