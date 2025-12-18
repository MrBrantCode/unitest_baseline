"""
QUESTION:
Create a function `merge_arrays` that merges two sorted arrays into a single sorted array in O(n) time, where n is the total number of elements in both arrays. The function should handle the case when one of the arrays is empty. The input arrays will be sorted in ascending order and contain only integers. The function should return a new sorted array containing all elements from the input arrays.
"""

def merge_arrays(arr1, arr2):
    merged_array = []
    while arr1 and arr2:  
        if arr1[0] < arr2[0]:
            merged_array.append(arr1.pop(0))
        else:
            merged_array.append(arr2.pop(0))
    merged_array.extend(arr1)
    merged_array.extend(arr2)
    return merged_array