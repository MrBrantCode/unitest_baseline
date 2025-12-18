"""
QUESTION:
Implement a function `insertion_sort_descending(arr)` that sorts an array of integers in descending order using a modified version of the insertion sort algorithm. The function should take an array of integers as input, sort it in descending order, and return the sorted array. The array can contain duplicate values and should be sorted in-place.
"""

def insertion_sort_descending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr