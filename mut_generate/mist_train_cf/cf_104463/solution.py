"""
QUESTION:
Write a function `merge_arrays` that merges two arrays `arr1` and `arr2`. The merged array should contain all elements from both arrays, alternating between elements from `arr1` and `arr2`. If one array has more elements than the other, the remaining elements should be appended to the end of the merged array.
"""

def merge_arrays(arr1, arr2):
    merged = []
    len1 = len(arr1)
    len2 = len(arr2)
    min_len = min(len1, len2)
    
    for i in range(min_len):
        merged.append(arr1[i])
        merged.append(arr2[i])
    
    if len1 > len2:
        for i in range(min_len, len1):
            merged.append(arr1[i])
    elif len2 > len1:
        for i in range(min_len, len2):
            merged.append(arr2[i])
    
    return merged