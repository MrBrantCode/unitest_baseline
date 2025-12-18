"""
QUESTION:
Implement the `bubble_sort` function, which sorts an array of numbers in ascending order using the bubble sort algorithm. The function should take an array as input and return the sorted array without using any built-in sorting functions or external libraries.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr