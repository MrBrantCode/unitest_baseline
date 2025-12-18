"""
QUESTION:
Write a function named `sort_array_descending` that takes an array of integers as input and returns the array sorted in descending order. The function should be efficient and have a minimal time complexity.
"""

def sort_array_descending(arr):
    n = len(arr)
    # Iterate through all elements in the array
    for i in range(n):
        # Flag variable to check if any swap is performed in the current iteration
        swap = False
        # Iterate through the array from 0 to n-i-1
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap the elements if the current element is less than the next element
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        # If no swap is performed in the current iteration, the array is already sorted
        if not swap:
            break
    return arr