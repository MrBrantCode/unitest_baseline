"""
QUESTION:
Write a function named bubble_sort to sort an array in ascending order without using built-in sorting functions or libraries. The function should have a time complexity of O(n^2) and take an array as input.
"""

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr