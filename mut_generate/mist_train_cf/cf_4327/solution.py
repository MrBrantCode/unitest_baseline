"""
QUESTION:
Implement a function called `bubbleSort` that takes in an array of integers as a parameter and returns the sorted array in ascending order using a modified version of the Bubble Sort algorithm. The function should have a time complexity of O(n^2) and efficiently handle arrays of up to 10000 elements without using any built-in sorting methods or libraries. The function should also optimize the bubble sort algorithm by adding a flag to check if any swaps were made in a pass.
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr