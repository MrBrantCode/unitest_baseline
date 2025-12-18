"""
QUESTION:
Implement the `insertion_sort` function, which sorts an array of integers in ascending order using the insertion sort algorithm. The function should take an array of integers as input and return the sorted array. Ensure that the time complexity of the implementation is O(n^2), where n is the number of elements to be sorted.
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