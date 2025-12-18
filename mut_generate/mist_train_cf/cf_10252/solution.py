"""
QUESTION:
Implement a function `sort_list(arr)` that sorts a list of numbers in ascending order using the quicksort algorithm with a time complexity of O(n log n). The input list may contain duplicates and negative numbers, and the function should handle these cases correctly.
"""

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def sort_list(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr