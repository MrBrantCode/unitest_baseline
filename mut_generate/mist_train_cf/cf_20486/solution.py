"""
QUESTION:
Implement a function named `bubble_sort_descending` that sorts an array of integers in descending order using the bubble sort technique. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swapping occurs during the iteration
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swapping occurred during the iteration, the array is already sorted
        if not swapped:
            break
    return arr