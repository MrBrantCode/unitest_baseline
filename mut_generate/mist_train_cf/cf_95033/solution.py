"""
QUESTION:
Implement a function `quicksort(arr)` to sort an array of integers in ascending order without using any built-in sorting functions or libraries. The function should have a time complexity of O(n log n) and a space complexity of O(1). The input is an array of integers and the function should sort the array in-place.
"""

def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr):
    stack = [(0, len(arr) - 1)]  # Using a stack to simulate recursion
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_idx = partition(arr, low, high)
            stack.append((low, pivot_idx - 1))
            stack.append((pivot_idx + 1, high))