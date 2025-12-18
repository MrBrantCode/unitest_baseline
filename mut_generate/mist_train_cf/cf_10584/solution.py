"""
QUESTION:
Write a function called `bubble_sort` that takes an array of integers as input, sorts it in ascending order using the Bubble Sort technique, and returns the sorted array. The implementation should be efficient and not use any built-in sorting functions or libraries.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr