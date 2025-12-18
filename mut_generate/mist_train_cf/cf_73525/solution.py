"""
QUESTION:
Implement a custom sorting algorithm that sorts an unsorted array of integers in ascending order, handling potential duplicate values and negative integers without using any pre-built sorting functions.
"""

def sort_array(arr):
    for i in range(len(arr)):
        # Assume the element at the current index is the smallest
        # for the unsorted part of the array
        min_idx = i
    
        # Iterate through the unsorted part of the array
        for j in range(i+1, len(arr)):
            # If we find an element that is smaller than the previously
            # assumed smallest, update min_idx
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the current element with the smallest element from the
        # unsorted part of the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr