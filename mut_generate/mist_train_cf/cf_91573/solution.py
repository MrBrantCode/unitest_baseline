"""
QUESTION:
Create a function named `bubble_sort_descending` that takes an array of integers as input and returns the array sorted in descending order. The array can contain integers ranging from -1000 to 1000 and its length will be between 1 and 1000. The function should not use any built-in sorting functions or methods, and should only use basic operations such as loops, conditional statements, and variable assignments.
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