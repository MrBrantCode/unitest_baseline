"""
QUESTION:
Write a program with two functions, `bubble_sort_asc` and `bubble_sort_desc`, to sort an array of integers in ascending and descending order, respectively, without using any built-in sorting functions or libraries. The functions should take an array as input and return the sorted array, and the original array should not be modified.
"""

def entance(arr, mode):
    n = len(arr)
    if mode == 'asc':
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    elif mode == 'desc':
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr