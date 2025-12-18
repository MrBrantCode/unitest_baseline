"""
QUESTION:
Implement a function called `bubble_sort_descending` that takes an array of numbers as input, sorts the array in descending order using the bubble sort algorithm, and groups duplicates together. The function should handle arrays containing both positive and negative numbers, as well as floating-point numbers.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr