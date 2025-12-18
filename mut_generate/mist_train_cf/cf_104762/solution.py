"""
QUESTION:
Implement a function called `bubble_sort` that sorts a list of integers in descending order without using any built-in sorting functions or libraries. The function should take a list of integers as input and return the sorted list.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr