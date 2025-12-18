"""
QUESTION:
Write a function `merge_arrays(arr1, arr2)` that merges two sorted arrays `arr1` and `arr2` into a single sorted array. The function should handle cases where one of the arrays is empty, and it must maintain a time complexity of O(n), where n is the total number of elements in both arrays. The function should return the merged array.
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