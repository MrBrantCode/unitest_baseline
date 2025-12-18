"""
QUESTION:
Implement an iterative quicksort function in Python that takes an array as input, sorts the array in ascending order using the quicksort algorithm, and returns the sorted array. The function must not use any built-in sorting functions or libraries and must have an average time complexity of O(n log n).
"""

def quicksort(arr):
    stack = []
    stack.append((0, len(arr)-1))

    while stack:
        low, high = stack.pop()

        if low >= high:
            continue

        pivot_index = partition(arr, low, high)
        stack.append((low, pivot_index-1))
        stack.append((pivot_index+1, high))

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1