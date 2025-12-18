"""
QUESTION:
Implement the `quick_sort` function to sort a list of numbers in ascending order using the quick sort algorithm. The function should have a time complexity of O(n log n), handle large input lists efficiently, and correctly sort lists containing duplicates and negative numbers. The function should also handle cases where the input list is already sorted.
"""

def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)
    return arr

def _quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        _quick_sort(arr, low, pivot - 1)
        _quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1