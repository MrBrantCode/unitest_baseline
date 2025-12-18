"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of at least 10,000 positive integers as input and returns the sorted array from smallest to largest using the bubble sort algorithm.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr