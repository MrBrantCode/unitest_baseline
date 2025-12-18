"""
QUESTION:
Implement a function named bubble_sort_optimized that takes a list of integers as input and returns the sorted list using the bubble sort algorithm with a flag to check if any swaps occurred during each pass. The function should optimize the time complexity in the best-case scenario when the array is already sorted. Ensure that the function has a time complexity of O(n) in the best case and O(n^2) in the worst case, and a space complexity of O(1).
"""

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr