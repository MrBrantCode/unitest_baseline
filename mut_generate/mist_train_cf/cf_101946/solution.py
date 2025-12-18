"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers in increasing order, allowing for duplicate elements, and with a time complexity of O(n^2).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr