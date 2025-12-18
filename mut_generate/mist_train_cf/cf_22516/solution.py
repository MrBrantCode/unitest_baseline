"""
QUESTION:
Write a function named `merge_sort` that sorts an array of integers in descending order with a time complexity of O(n log n) or better. The function should correctly handle duplicate integers by preserving their relative order in the sorted array. The input is an array of integers and the output is the sorted array.
"""

def merge_sort(arr):
    # Base case: if the array has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the two sorted halves
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Compare elements from both halves and append them in descending order
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Append any remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged