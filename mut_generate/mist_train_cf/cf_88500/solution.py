"""
QUESTION:
Implement a recursive Merge Sort algorithm to sort an unsorted array of numbers in ascending order without using any comparison-based sorting algorithm. The function should be named `merge_sort` and take an array `arr` as input. The implementation should not use any built-in sorting functions or libraries and should not use extra space for merging the arrays. The time complexity of the solution should be O(n log n) and should be able to handle arrays with duplicate elements and very large input arrays efficiently.
"""

def merge_sort(arr):
    # Base case: if the array has only one element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Copy any remaining elements from the left half
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # Copy any remaining elements from the right half
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    return arr