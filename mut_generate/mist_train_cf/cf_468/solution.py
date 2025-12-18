"""
QUESTION:
Implement the `bubble_sort` function to sort a given array in ascending order using Bubble sort. The function should not use any additional data structures or built-in sorting functions and must have a time complexity of O(n^2) and space complexity of O(1).
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr