"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of integers as input and returns the array sorted in descending order using the bubble sort algorithm. The function should modify the original array and return it. The array can contain duplicate values.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr