"""
QUESTION:
Implement a function called `insertion_sort` that sorts an array of integers in ascending order using the insertion sort algorithm. The function should take an array of integers as input and return the sorted array.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr