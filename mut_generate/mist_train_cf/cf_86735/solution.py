"""
QUESTION:
Write a function `computeMedian(arr)` that takes an array of integers `arr` as input, where the length of `arr` is an odd number greater than 1, and returns the median of the array. The function should have a time complexity of O(n log n), a space complexity of O(1), and should not use any built-in sorting functions or data structures. The function should be able to handle arrays with a very large number of elements efficiently.
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSelect(arr, low, high, k):
    if low == high:
        return arr[low]
    pivotIndex = partition(arr, low, high)
    if k == pivotIndex:
        return arr[k]
    elif k < pivotIndex:
        return quickSelect(arr, low, pivotIndex - 1, k)
    else:
        return quickSelect(arr, pivotIndex + 1, high, k)

def computeMedian(arr):
    n = len(arr)
    medianIndex = (n + 1) // 2 - 1
    return quickSelect(arr, 0, n - 1, medianIndex)