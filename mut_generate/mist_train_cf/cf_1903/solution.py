"""
QUESTION:
Write a function named `sort_array` that takes an array as input and returns the array sorted in descending order using a single for loop.
"""

def sort_array(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr