"""
QUESTION:
Write a function named `insertion_sort` that takes an array of integers as input and returns the array sorted in ascending order. The function must implement the insertion sort algorithm from scratch, without using any built-in sorting functions or methods.
"""

def entrance(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr