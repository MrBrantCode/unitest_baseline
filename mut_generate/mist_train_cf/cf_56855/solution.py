"""
QUESTION:
Write a function named `bubbleSort` that sorts an array in ascending order using the bubble sort algorithm. The function should take one argument, `array`, which is the input list to be sorted. The function should return the sorted array. The function should also be optimized to stop early if the array is already sorted.
"""

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array