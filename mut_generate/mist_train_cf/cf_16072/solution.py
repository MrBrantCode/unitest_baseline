"""
QUESTION:
Implement a function called `merge_sort` that sorts the given array of integers in increasing order. The function should not use any built-in sorting functions or libraries, have a time complexity of less than O(n log n), and a space complexity of less than O(log n). The input to the function will be an array of integers and the output should be the sorted array.
"""

def merge_sort(arr):
    # Base case: if the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Compare elements from the two halves and merge them in ascending order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add the remaining elements from the left half (if any)
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Add the remaining elements from the right half (if any)
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged