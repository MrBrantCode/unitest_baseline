"""
QUESTION:
Implement the insertion sort algorithm in Python. The function should be named `insertionSort` and it should take one argument `arr`, which is a list of integers. The function should return the sorted list of integers. The implementation should not use any built-in sorting functions or methods.
"""

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    return arr