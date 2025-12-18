"""
QUESTION:
Implement a function `bubble_sort(arr)` that takes an array of integers as input and returns the sorted array in ascending order using the bubble sort algorithm. The function should have a time complexity of O(n^2) or worse, handle duplicate integers, and preserve their original order. The function should not use any built-in sorting functions or libraries.
"""

def entrance(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr