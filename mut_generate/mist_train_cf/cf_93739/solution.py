"""
QUESTION:
Implement a stable sorting algorithm that sorts a list of integers in descending order. The algorithm should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. The function should be named `bubble_sort` and take a list `arr` as input.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr