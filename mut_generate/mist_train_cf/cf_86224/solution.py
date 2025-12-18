"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of integers as input, sorts the array in increasing order using a time complexity of O(n^2), and returns the sorted array. The array may contain duplicate elements.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr