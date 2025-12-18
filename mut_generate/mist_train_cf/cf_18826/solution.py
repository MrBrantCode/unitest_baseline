"""
QUESTION:
Implement a function named `merge_sort` that takes a list of integers as input, sorts it in ascending order while preserving the relative order of equal elements, and returns the sorted list. The function should have a time complexity of O(n log n) and should not use any built-in sorting functions or data structures.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    merged = merge(left_half, right_half)
    return merged

def merge(left, right):
    result = []
    i, j = 0, 0
    
    # Compare elements from both halves and place them in the correct order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append any remaining elements from the left or right half
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result