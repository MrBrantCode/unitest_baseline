"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of integers as input and returns the list sorted in ascending order. You must use the Bubble Sort algorithm and cannot use any built-in sorting functions or libraries. The input list can contain any number of elements.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr