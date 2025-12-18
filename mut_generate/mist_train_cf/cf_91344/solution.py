"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array using the bubble sort algorithm. The function should take an array as input and return the sorted array. The bubble sort algorithm should repeatedly compare adjacent elements and swap them if they are in the wrong order. The function should use a temporary variable to correctly swap the elements.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr