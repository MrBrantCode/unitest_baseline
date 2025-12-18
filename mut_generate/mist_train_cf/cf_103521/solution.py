"""
QUESTION:
Write a function named `bubble_sort` that sorts a list of integers in ascending order using the Bubble Sort algorithm. The function should take a list of integers as input and return the sorted list.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr