"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of integers as input and returns the sorted list in ascending order. You cannot use built-in sorting functions, libraries, or additional data structures. The function should modify the input list in-place.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swapping occurs in the current pass
        swapped = False
        for j in range(0, n-i-1):
            # Swap elements if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swapping occurred in the current pass, the array is already sorted
        if not swapped:
            break
    return arr