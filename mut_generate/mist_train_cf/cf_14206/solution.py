"""
QUESTION:
Create a function called `bubble_sort` that takes a list of integers as input and returns the sorted list in ascending order. The function should have a time complexity of O(n^2) and not use any built-in sorting functions or libraries. The input list can contain duplicate values and negative numbers.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr