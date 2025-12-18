"""
QUESTION:
Implement the `bubble_sort` function to sort an array of integers in ascending order. The input array should contain at least 5 integers and at most 100 integers, with each integer within the range of -1000 to 1000. You cannot use any built-in sorting functions or libraries. The function should return the sorted array as output.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr