"""
QUESTION:
Implement the function `bubble_sort(arr)` to sort an array of integers in ascending order using the bubble sort algorithm. The function should take an array of integers as input and return the sorted array. Assume the input array will contain at least 2 elements and at most 10 elements.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr