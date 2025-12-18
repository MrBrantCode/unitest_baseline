"""
QUESTION:
Write a function named `bubble_sort` that takes a list of positive integers as input and returns the sorted list in ascending order without using any built-in sorting functions or methods, with a time complexity of O(n^2).
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr