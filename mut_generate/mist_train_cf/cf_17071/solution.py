"""
QUESTION:
Implement a function `bubble_sort(arr)` that takes a list of numbers as input and returns the sorted list using the bubble sort algorithm. The function should have a time complexity of O(n^2) in the worst and average case.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr