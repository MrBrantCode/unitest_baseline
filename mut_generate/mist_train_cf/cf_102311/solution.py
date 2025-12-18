"""
QUESTION:
Create a function called "sort_array_descending" that takes in an array as a parameter and returns the sorted array in descending order. The function should implement the Bubble Sort algorithm without using any built-in sorting functions.
"""

def sort_array_descending(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr