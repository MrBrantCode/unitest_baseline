"""
QUESTION:
Implement a function called `bubble_sort` that sorts an array in-place, using the Bubble Sort algorithm, with a time complexity of O(n^2) and a space complexity of O(1). The function should take a list of integers as input and return the sorted list. The algorithm should put elements in the right place by repeatedly swapping adjacent elements if they are in the wrong order. 

The function should include an optimization to track if any swaps have been made during each iteration, and if no swaps are made, the algorithm should terminate early.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swaps = False  # Add a flag to track swaps
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True  # Set flag to True if any swaps are made
        if not swaps:
            break  # If no swaps are made, terminate the algorithm early
    return arr