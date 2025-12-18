"""
QUESTION:
Create a function called `merge_sorted_arrays` that takes two sorted arrays `arr1` and `arr2` as input and returns a new sorted array that contains all elements from both arrays, with no duplicates, without using any built-in sorting functions. The function should achieve a time complexity of O(n), where n is the total number of elements in both arrays, and should not use any additional data structures or libraries. The input arrays can contain duplicate elements, but the resulting array should not.
"""

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if len(merged) == 0 or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if len(merged) == 0 or merged[-1] != arr2[j]:
                merged.append(arr2[j])
            j += 1
        else:
            if len(merged) == 0 or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
            j += 1
    
    while i < len(arr1):
        if len(merged) == 0 or merged[-1] != arr1[i]:
            merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if len(merged) == 0 or merged[-1] != arr2[j]:
            merged.append(arr2[j])
        j += 1
    
    return merged