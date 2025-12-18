"""
QUESTION:
Implement a function `merge_sort(arr)` that sorts the given array `arr` in ascending order. The array may contain duplicate elements. The function should:

* Not use any built-in sorting functions or algorithms
* Have a time complexity of O(n*log(n)) or better
* Be a stable sorting algorithm to preserve the relative order of elements with equal values
* Use a constant amount of additional memory
* Handle large input sizes efficiently

The input `arr` is a list of integers, and the output should be a sorted list of integers.
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