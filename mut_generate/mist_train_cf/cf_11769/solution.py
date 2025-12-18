"""
QUESTION:
Implement a function `bubble_sort` that takes an array of integers as input and returns the array in descending order. The function should use the bubble sort algorithm to sort the array.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr