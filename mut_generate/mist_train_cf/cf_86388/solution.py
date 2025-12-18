"""
QUESTION:
Write a function `optimized_sort(arr)` that takes an array `arr` as input and returns a new array with the elements sorted in ascending order, without any duplicates. The function should use a sorting algorithm with a time complexity of O(n log n). Note that you cannot use any built-in sorting functions or libraries.
"""

def optimized_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = optimized_sort(left)
    right = optimized_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    merged = set()
    i = 0
    j = 0
    
    # Compare and merge the elements from left and right halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.add(left[i])
            i += 1
        elif left[i] > right[j]:
            merged.add(right[j])
            j += 1
        else:
            merged.add(left[i])
            i += 1
            j += 1
    
    # Append the remaining elements
    while i < len(left):
        merged.add(left[i])
        i += 1
    
    while j < len(right):
        merged.add(right[j])
        j += 1
    
    # Convert the set back to a list and sort it
    return sorted(list(merged))