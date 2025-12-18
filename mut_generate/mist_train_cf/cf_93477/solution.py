"""
QUESTION:
Write a function `bubble_sort(arr)` that takes a list of integers as input and returns the sorted list in ascending order. The function should implement a sorting algorithm without using any built-in sorting functions or libraries. The input list is guaranteed to contain only integers, and the output should be a list of integers in ascending order.
"""

def entance(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr