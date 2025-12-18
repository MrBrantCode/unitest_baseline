"""
QUESTION:
Implement the `bubbleSort` function to sort a given list of integers in descending order without using any built-in sorting functions. The function should take a list of integers as input and return the sorted list.
"""

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr