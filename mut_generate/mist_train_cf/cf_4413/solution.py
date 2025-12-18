"""
QUESTION:
Implement the `customSort` function to sort an array of integers in ascending order with a time complexity of O(n^2) without using built-in sorting functions or libraries. The input array can contain positive and negative integers and will not be empty.
"""

def customSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr