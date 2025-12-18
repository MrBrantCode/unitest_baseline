"""
QUESTION:
Create a function mergeArrays(arr1, arr2) that takes two sorted arrays as input and returns a new sorted array containing all elements from arr1 and arr2. The solution must have a time complexity of O(n), where n is the total number of elements in both arr1 and arr2, and cannot use any built-in sorting functions.
"""

def mergeArrays(arr1, arr2):
    merged = []
    pointer1 = 0
    pointer2 = 0
    
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] < arr2[pointer2]:
            merged.append(arr1[pointer1])
            pointer1 += 1
        else:
            merged.append(arr2[pointer2])
            pointer2 += 1
    
    # Add remaining elements from arr1, if any
    while pointer1 < len(arr1):
        merged.append(arr1[pointer1])
        pointer1 += 1
    
    # Add remaining elements from arr2, if any
    while pointer2 < len(arr2):
        merged.append(arr2[pointer2])
        pointer2 += 1
    
    return merged