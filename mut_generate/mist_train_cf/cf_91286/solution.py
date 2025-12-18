"""
QUESTION:
Implement a function called `bubble_sort` that takes an array of integers as input and returns the sorted array from smallest to largest using the bubble sort algorithm. The function should use a loop to iterate through the array, compare adjacent elements, and swap their positions if they are out of order. The function should minimize unnecessary comparisons and swaps by only iterating until the array is fully sorted.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr