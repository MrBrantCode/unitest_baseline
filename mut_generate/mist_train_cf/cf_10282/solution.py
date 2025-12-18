"""
QUESTION:
Implement a function named `bubble_sort_descending` that takes an array of integers as input and returns the array sorted in descending order without using any built-in sorting functions.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr