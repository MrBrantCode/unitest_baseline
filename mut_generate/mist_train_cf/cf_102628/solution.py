"""
QUESTION:
Implement a function named `modified_insertion_sort` that takes an array of integers as input and returns the array sorted in descending order. The function should use a modified version of the insertion sort algorithm.
"""

def modified_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr