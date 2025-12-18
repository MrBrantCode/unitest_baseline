"""
QUESTION:
Write a function named `non_increasing_sort` that sorts a list of integers in non-increasing order without using any built-in sorting functions or libraries. The function should have a time complexity of O(n^2) and not use any additional data structures.
"""

def non_increasing_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr