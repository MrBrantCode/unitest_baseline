"""
QUESTION:
Create a function named `sort_array` or `bubbleSort` that takes an array of integers as input and returns the array sorted in ascending order without using built-in sorting functions or libraries. The function should be able to handle arrays containing both positive and negative integers.
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr