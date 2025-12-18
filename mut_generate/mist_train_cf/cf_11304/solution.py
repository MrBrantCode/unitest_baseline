"""
QUESTION:
Implement the `bubble_sort` function to sort an array of integers in non-decreasing order without using any built-in sorting functions or libraries. The function should handle cases where the input array is empty or contains duplicate elements, and have a time complexity of O(n^2).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swapping is done in this iteration
        swapped = False
        for j in range(0, n-i-1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swapping is done in this iteration, the array is already sorted
        if not swapped:
            break
    return arr