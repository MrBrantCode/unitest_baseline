"""
QUESTION:
Write a function called "sort_array_descending" that takes an array as a parameter and returns the sorted array in descending order. The function must implement the Bubble Sort algorithm and cannot use any built-in sorting functions. The array is to be sorted in place and the function should return the sorted array.
"""

def sort_array_descending(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr