"""
QUESTION:
Implement the function `computeMedian(arr)` that computes the median of an array of n integers, where n is an odd number greater than 1. The function should not use any built-in sorting functions or data structures. The array may contain duplicate elements. The time complexity should be O(n log n) and the space complexity should be O(1).
"""

def computeMedian(arr):
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

    n = len(arr)
    medianIndex = (n + 1) // 2 - 1
    return quickSelect(arr, 0, n - 1, medianIndex)