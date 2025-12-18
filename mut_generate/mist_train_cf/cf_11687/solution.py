"""
QUESTION:
Implement a function named bubble_sort that takes an array of integers as input and returns the sorted array in ascending order without using any built-in sorting methods or functions.
"""

def bubble_sort(arr):
    length = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr