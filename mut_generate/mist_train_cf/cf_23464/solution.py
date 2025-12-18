"""
QUESTION:
Implement a function named `SortArray` that takes an array of integers as input and returns a sorted array in ascending order. The function should use a sorting algorithm to sort the input array in-place.
"""

def SortArray(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array