"""
QUESTION:
Write a function called `sort_array` that takes an array of integers as input and returns the same array sorted in ascending order without using any built-in sorting functions or libraries.
"""

def sort_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr