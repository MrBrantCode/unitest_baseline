"""
QUESTION:
Implement a function named `sort_descending(arr)` that takes a list of integers as input and sorts it in descending order without using any built-in sorting functions or methods, and without using any additional data structures. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def sort_descending(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    quicksort(arr, 0, len(arr) - 1)