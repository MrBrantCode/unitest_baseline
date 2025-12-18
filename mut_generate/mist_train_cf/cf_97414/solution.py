"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of integers as input and returns the list in ascending order without using any built-in sorting functions or libraries, and without using any additional data structures.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr