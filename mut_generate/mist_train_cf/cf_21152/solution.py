"""
QUESTION:
Implement a function `merge_sort(arr)` that sorts an array of integers in ascending order using a recursive approach with a time complexity of O(nlogn). The function must not use any built-in sorting functions or libraries and should handle duplicate values correctly while maintaining their relative order in the sorted array. The function should also use constant space complexity (O(1)) for auxiliary data structures.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged