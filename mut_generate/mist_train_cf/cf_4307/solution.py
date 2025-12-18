"""
QUESTION:
Implement a function named `merge_sort` that sorts a list of elements in either ascending or descending order without using any built-in sorting functions. The function should take two parameters: the input list `arr` and an optional boolean flag `ascending` (default value is `True`) to indicate the sorting order. The function should return the sorted list.
"""

def merge_sort(arr, ascending=True):
    # Base case: if the input list has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the input list into two equal-sized sublists
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort each sublist
    left = merge_sort(left, ascending)
    right = merge_sort(right, ascending)
    
    # Merge the two sorted sublists back together
    return merge(left, right, ascending)

def merge(left, right, ascending=True):
    merged = []
    i, j = 0, 0
    
    # Compare and add elements from both sublists to the merged list
    while i < len(left) and j < len(right):
        if (ascending and left[i] <= right[j]) or (not ascending and left[i] >= right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add any remaining elements from either sublist to the merged list
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged