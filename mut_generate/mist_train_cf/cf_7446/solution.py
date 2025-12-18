"""
QUESTION:
Implement a function named `merge_sort` that takes a list of numbers as input, sorts them in descending order without using any built-in sorting functions or libraries, and returns the sorted list. The function should have a time complexity of O(n log n) and a space complexity of O(log n), and it should be a stable sort, maintaining the relative order of elements with equal values during the sorting process.
"""

def merge_sort(arr):
    # Base case: if the list has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Merge the two sublists into a sorted list
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add the remaining elements from the left sublist
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Add the remaining elements from the right sublist
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged