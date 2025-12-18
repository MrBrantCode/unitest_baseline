"""
QUESTION:
Implement a function called `bubble_sort` that takes an array of integers as input and returns the sorted array in increasing order. The function should implement the bubble sort algorithm and handle cases where the array is empty or has only one element. Do not use any built-in sorting functions or libraries.
"""

def entrance(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr