"""
QUESTION:
Write a function named `bubble_sort` that sorts an array of numbers in ascending order using the bubble sort algorithm and optimizes the process by returning immediately if the array is already sorted. The function should take an array as input and return the sorted array.
"""

def bubble_sort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        n -= 1
    return arr