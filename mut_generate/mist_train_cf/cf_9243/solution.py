"""
QUESTION:
Implement a function `insertion_sort_desc` that takes an array of integers as input and returns the array sorted in descending order using the insertion sort algorithm. The function should modify the input array in-place.
"""

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr