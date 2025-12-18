"""
QUESTION:
Implement a function named `bubble_sort` that takes an array as input and returns the array in ascending order without using any built-in sorting functions. The function must achieve this with a time complexity of O(n log n) or better and a space complexity of O(1). Additionally, the function should only use a maximum of two loops in its solution.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps are made in this pass
        swapped = False
        for j in range(0, n-i-1):
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps are made, the array is already sorted
        if not swapped:
            break
    return arr