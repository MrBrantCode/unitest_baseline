"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts an array of integer elements in ascending order without using any built-in sorting functions. The array can contain both positive and negative values.
"""

def entrance(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr