"""
QUESTION:
Implement a function named bubble_sort that sorts a list of integers in descending order without using any built-in sorting functions or libraries. The function should have a time complexity of O(n^2).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr