"""
QUESTION:
Implement a function called `sort_array` that takes an array of at least 10 positive integers between 1 and 100 (inclusive) and returns the sorted array in ascending order without using any built-in sorting methods or functions.
"""

def sort_array(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr