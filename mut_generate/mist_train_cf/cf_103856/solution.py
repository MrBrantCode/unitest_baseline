"""
QUESTION:
Write a function named `find_max` that finds the maximum element in an unsorted array without using any built-in sorting functions, and the time complexity of the function should be O(n^2).
"""

def find_max(arr):
    n = len(arr)
    max_val = arr[0]
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > max_val:
                max_val = arr[j]
    return max_val