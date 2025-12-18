"""
QUESTION:
Create a function called "merge_arrays" that takes in two sorted arrays, arr1 and arr2, of sizes n and m respectively, and merges them into a new sorted array of size n + m. The input arrays are sorted in ascending order and can contain positive, negative, or zero values, as well as duplicates. The function should have a time complexity of O(n + m).
"""

def merge_arrays(arr1, arr2):
    merged = []
    pointer1 = 0
    pointer2 = 0
    
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