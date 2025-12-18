"""
QUESTION:
Implement a function `bubble_sort(arr)` that takes an array as input and returns the array sorted in ascending order without using any built-in sorting functions. The time complexity of the solution should be O(n^2) or better.
"""

def entance(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr