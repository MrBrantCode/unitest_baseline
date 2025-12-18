"""
QUESTION:
Implement a function named `bubble_sort` that performs bubble sort on an array of integers in ascending order. The input array can contain duplicate elements and may have a length of up to 10^6. The implementation should have a time complexity of O(n^2) and should not use any built-in sorting functions, libraries, additional data structures, or arrays to assist in the sorting process.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr