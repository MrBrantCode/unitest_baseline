"""
QUESTION:
Create a function called `sort_list_descending` that takes a list of integers as input and returns the sorted list in descending order without using any built-in sorting functions or methods.
"""

def sort_list_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr