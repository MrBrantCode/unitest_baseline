"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts an array of positive integers in ascending order using the bubble sort algorithm with a single outer loop and a time complexity of O(n^2). The array should have a length between 5 and 1000 (inclusive).
"""

def entance(arr):
    n = len(arr)
    for i in range(n):
        # Set a flag to check if any swaps are made in this iteration
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap arr[j] and arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swaps are made in this iteration, the array is already sorted
        if not swapped:
            break

    return arr