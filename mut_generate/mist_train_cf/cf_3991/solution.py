"""
QUESTION:
Implement a function called `sort_descending` that takes a list of integers as input, sorts it in descending order, and returns the sorted list. The function must not use any built-in sorting functions or methods, nor any additional data structures. It should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def sort_descending(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    quicksort(0, len(arr) - 1)