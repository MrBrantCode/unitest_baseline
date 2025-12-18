"""
QUESTION:
Implement a function `merge_arrays` that takes two sorted arrays `arr1` and `arr2` and returns a new sorted array containing all elements from both arrays. The function should have a time complexity of O(n), where n is the total number of elements in both arrays, and a space complexity of O(1). The function should handle cases when one or both arrays are empty and should not modify the original arrays. The elements in the merged array should be in non-decreasing order.
"""

def merge_arrays(arr1, arr2):
    result = []
    i, j = 0, 0
    
    # Merge smaller elements first
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # If there are remaining elements in arr1, append them to result
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    # If there are remaining elements in arr2, append them to result
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result