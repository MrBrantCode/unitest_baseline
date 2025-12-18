"""
QUESTION:
Write a function `bubbleSortDescending(arr)` that sorts an array of integers in descending order using the bubble sort algorithm. The function should take an array of integers as input and return the sorted array.
"""

def bubbleSortDescending(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr