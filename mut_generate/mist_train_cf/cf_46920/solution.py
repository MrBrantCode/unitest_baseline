"""
QUESTION:
Implement a function `descending_sort` that takes an array of integers as input, sorts the array in descending order using the bubble sort algorithm, and returns the smallest element in the array. Note that the function should be designed such that it can be used to find the smallest element by sorting the array in descending order first.
"""

def descending_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[-1]