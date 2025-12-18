"""
QUESTION:
Implement a function named simpleSort that takes an array of integers as input and returns the array sorted in ascending order. The function must have a time complexity of O(n^2) and cannot use any built-in sorting functions or data structures. The input array will contain integers ranging from -1000 to 1000.
"""

def simpleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr