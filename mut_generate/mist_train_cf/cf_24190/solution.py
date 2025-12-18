"""
QUESTION:
Implement a function named `bubbleSort` that takes an array of integers as input, sorts it in ascending order using the bubble sort algorithm, and returns the sorted array.
"""

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array