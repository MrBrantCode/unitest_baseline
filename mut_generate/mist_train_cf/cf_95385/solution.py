"""
QUESTION:
Implement the `merge_sort` function to sort a list of integers with a time complexity of O(n log n). The function should handle duplicate elements efficiently and preserve their relative order. You are not allowed to use any built-in sorting functions or data structures. The function should take a list of integers as input and return the sorted list.
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