"""
QUESTION:
Implement a function named `sort` that takes an array of elements as input and returns the sorted array. The sorting algorithm should use recursion and include a `partition` function to divide the array into two subarrays based on a chosen pivot value. The function should handle cases where the input array is empty or contains only one element without making any unnecessary recursive calls.
"""

def sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def recursiveSort(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            recursiveSort(arr, low, pivot - 1)
            recursiveSort(arr, pivot + 1, high)

    if len(arr) <= 1:
        return arr
    else:
        recursiveSort(arr, 0, len(arr) - 1)
        return arr