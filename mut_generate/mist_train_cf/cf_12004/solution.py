"""
QUESTION:
Implement a function `bubble_sort_descending(arr)` that sorts an array of integers in descending order using the bubble sort algorithm. The function should take an array of integers as input and return the sorted array.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr