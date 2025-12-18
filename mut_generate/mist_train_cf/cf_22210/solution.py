"""
QUESTION:
Implement a function named `merge_sort` that sorts an array of integers in ascending order. The array may contain duplicate elements. The function should not use any built-in sorting functions or algorithms, have a time complexity of O(n*log(n)) or better, be stable to preserve the relative order of elements with equal values, and use a constant amount of additional memory to minimize the use of additional data structures.
"""

def merge_sort(arr):
    # Base case: if the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves back together
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    
    # Compare elements from the left and right halves and add the smaller one to the merged list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add the remaining elements from the left half, if any
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Add the remaining elements from the right half, if any
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged