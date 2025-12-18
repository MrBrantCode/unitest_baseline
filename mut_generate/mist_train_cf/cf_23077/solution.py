"""
QUESTION:
Implement a function named `quicksort` that takes a list of integers as input and returns the sorted list in descending order. The function should have a time complexity of O(n log n) and should not use any additional data structures or recursion.
"""

def entance(arr):
    stack = []
    low = 0
    high = len(arr) - 1
    stack.append((low, high))

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1