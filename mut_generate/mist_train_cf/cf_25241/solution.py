"""
QUESTION:
Implement a function called `bubble_sort` that takes an array of integers as input, sorts the array using the bubble sort technique, and returns the sorted array. The function should be able to handle arrays of varying lengths and containing duplicate values. The array is sorted in ascending order.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr