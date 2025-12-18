"""
QUESTION:
Write a function `bubble_sort(arr)` that sorts a list of integers in descending order. The function should have a time complexity of O(n^2) and cannot use any built-in sorting functions or libraries.
"""

def entance(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr