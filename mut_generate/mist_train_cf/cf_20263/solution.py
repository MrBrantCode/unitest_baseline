"""
QUESTION:
Create a function `bubble_sort_descending` that takes an array of integers as input, sorts it in descending order using the bubble sort algorithm, and returns the sorted array. The function should not use any built-in sorting methods.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr