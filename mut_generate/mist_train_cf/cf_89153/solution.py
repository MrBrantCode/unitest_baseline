"""
QUESTION:
Implement a function `bubble_sort` that performs bubble sort on an array of integers in ascending order. The function should not use any built-in sorting functions or libraries and should have a time complexity of O(n^2), where n is the length of the input array. The function should also not use any additional data structures or arrays to assist in the sorting process, and all sorting operations should be performed directly on the input array.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr