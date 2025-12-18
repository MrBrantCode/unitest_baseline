"""
QUESTION:
Construct a function `sort_array_ascending` that sorts an array of integers in ascending order using a nested loop to compare and swap elements, without using the `sort()` or `sorted()` function. The function should take an array as input and return the sorted array.
"""

def sort_array_ascending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr