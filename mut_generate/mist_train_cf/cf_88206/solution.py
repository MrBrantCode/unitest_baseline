"""
QUESTION:
Write a function `findKthSmallest` that finds the Kth smallest element from a given array of N elements using a recursive algorithm. The solution should have a time complexity of O(NlogN) and must not use any sorting algorithms or built-in functions for sorting. The function should take an array `arr` and an integer `k` as input and return the Kth smallest element. Note that the array is 1-indexed, so the function should subtract 1 from `k` before making the recursive calls.
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
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickSelect(arr, low, pivot_index - 1, k)
    else:
        return quickSelect(arr, pivot_index + 1, high, k)

def findKthSmallest(arr, k):
    n = len(arr)
    return quickSelect(arr, 0, n - 1, k - 1)