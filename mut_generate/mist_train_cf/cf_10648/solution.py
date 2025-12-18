"""
QUESTION:
Implement a function named `non_increasing_sort` that takes a list of integers as input and returns the list sorted in non-increasing order. The function must have a time complexity of O(n^2) and should not use any built-in sorting functions, libraries, or additional data structures.
"""

def non_increasing_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr