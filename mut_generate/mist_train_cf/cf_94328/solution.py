"""
QUESTION:
Implement the `bubble_sort` function to sort an array of integers in ascending order. The input array should contain at least 10 and at most 1000 integers, with each integer within the range of -1000000 to 1000000. The function should not use any built-in sorting functions or libraries, and should return the sorted array.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr