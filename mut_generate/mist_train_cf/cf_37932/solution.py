"""
QUESTION:
Implement a function called `custom_sort` that sorts a list of integers in ascending order without using any built-in sorting functions or libraries. The function should take a list of integers as input and return the sorted list.
"""

from typing import List

def custom_sort(arr: List[int]) -> List[int]:
    # Implementing the bubble sort algorithm
    n = len(arr)
    for i in range(n):
        # Flag to check if any swap occurred in the current pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swap occurred, the array is already sorted
        if not swapped:
            break
    return arr