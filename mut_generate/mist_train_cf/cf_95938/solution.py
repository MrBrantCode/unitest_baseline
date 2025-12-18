"""
QUESTION:
Implement a function named `sort_array` that takes an array as input and returns the array with its elements in ascending order. The function should not use any built-in sorting functions. The time complexity should be O(n^2) or better, and the space complexity should be O(1). The input array may contain duplicate elements.
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