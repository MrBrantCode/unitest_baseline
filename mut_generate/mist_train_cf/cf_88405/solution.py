"""
QUESTION:
Implement a stable sorting function named `merge_sort` that takes two parameters: an array of elements and a boolean flag `ascending` to indicate the sorting order (default is `True` for ascending order). The function should be able to handle both ascending and descending sorting orders without using any built-in sorting functions or methods.
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