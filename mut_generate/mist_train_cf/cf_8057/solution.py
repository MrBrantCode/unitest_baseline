"""
QUESTION:
Define a function named `merge_sorted_arrays` that merges two sorted arrays `arr1` and `arr2` into a single sorted array. The merged array should be in non-decreasing order, not contain any duplicate elements, and have a time complexity of O(n log n), where n is the total number of elements in both arrays. The function should use constant space complexity and should not modify the original arrays.
"""

def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            merged_array.append(arr2[j])
            j += 1
        else:
            merged_array.append(arr1[i])
            i += 1
            j += 1
    
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    
    return merged_array