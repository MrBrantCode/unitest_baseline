"""
QUESTION:
Implement the `bubble_sort` function to sort an array in ascending order using the bubble sort algorithm. The function should take an array as input, sort it in-place using nested loops to compare and swap elements, and return the sorted array. Do not use the built-in `sort()` or `sorted()` functions.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr