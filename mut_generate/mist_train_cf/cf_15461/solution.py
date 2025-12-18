"""
QUESTION:
Write a function named bubble_sort that sorts a list of integers in descending order, has a time complexity of O(n^2), and does not use any built-in sorting functions or libraries. The function must be stable, preserving the relative order of equal elements in the sorted list.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr