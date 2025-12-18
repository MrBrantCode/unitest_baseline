"""
QUESTION:
Implement the `bubble_sort` function to sort a given list of numerical elements in ascending order using the bubble sort technique. The function should take a list of integers as input and return the sorted list. The input list is not guaranteed to be of any specific length, and the function should be able to handle lists of varying sizes. The function should also terminate early if the list is already sorted or becomes sorted during the sorting process.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Flag to indicate whether any swaps were made in the current pass
        swapped = False

        # Iterate through the unsorted part of the array, swapping adjacent elements if needed
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made in this pass, the array is already sorted
        if not swapped:
            break

    return arr