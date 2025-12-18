"""
QUESTION:
Write a function `findKthSmallest` that takes an array `arr` of N elements and an integer `k` as input, and returns the Kth smallest element in the array. The function should have a time complexity of O(NlogN) and should not use any sorting algorithms or built-in functions for sorting. The function should use a recursive algorithm to find the Kth smallest element.
"""

def findKthSmallest(arr, k):
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
        pivot_index = partition(arr, low, high)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickSelect(arr, low, pivot_index - 1, k)
        else:
            return quickSelect(arr, pivot_index + 1, high, k)

    n = len(arr)
    return quickSelect(arr, 0, n - 1, k - 1)