"""
QUESTION:
Implement a function `bubble_sort(arr)` that takes a list of integers as input, sorts it in ascending order using a stable sorting algorithm with a time complexity of O(n^2) or less, and a space complexity of O(n) or less, preserving the relative order of equal elements.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr