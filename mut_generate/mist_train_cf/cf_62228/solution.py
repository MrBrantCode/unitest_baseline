"""
QUESTION:
Implement the `bubbleSort` function, which takes a list of integers as input and returns the sorted list in ascending order using the Bubble Sort algorithm. The function should not use any built-in sorting methods and should only use basic operations like swapping elements.
"""

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array