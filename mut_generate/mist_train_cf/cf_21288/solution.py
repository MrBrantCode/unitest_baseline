"""
QUESTION:
Implement the `bubble_sort` function that takes an array as input, sorts its elements in ascending order using the bubble sort algorithm, and returns the sorted array. The array should have at least 5 elements, and no built-in sorting functions or libraries can be used.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr