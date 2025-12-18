"""
QUESTION:
Write a function named `bubble_sort_descending` that takes an array of integers as input and returns the sorted array in descending order without using any built-in sorting functions or methods. The input array will contain integers ranging from -1000 to 1000, and its length will be between 1 and 1000.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    
    for i in range(n):
        # flag to check if any swaps are made in the current iteration
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                # swap arr[j] and arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # if no swaps are made in the current iteration, the array is already sorted
        if not swapped:
            break
    
    return arr