"""
QUESTION:
Implement a function `insertion_sort` that sorts a multi-dimensional array of distinct numerical values in ascending order while maintaining the sequential relationship of duplicate values and removing non-numeric values. The function should take a multi-dimensional list as input and return a one-dimensional sorted list of numbers.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr