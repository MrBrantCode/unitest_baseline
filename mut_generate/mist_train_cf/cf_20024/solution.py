"""
QUESTION:
Implement a function `sort_array(arr)` that takes an array of integers as input, sorts the elements in ascending order without using any built-in sorting functions, and returns the sorted array. The function should have a time complexity of O(n^2) or better and a space complexity of O(1), allowing for the presence of duplicate elements in the array.
"""

def sort_array(arr):
    n = len(arr)
    # Perform n-1 passes
    for i in range(n - 1):
        # Flag to check if any swap occurred in this pass
        swapped = False
        # Compare adjacent elements and swap if necessary
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swap occurred in this pass, the array is already sorted
        if not swapped:
            break
    return arr