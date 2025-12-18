"""
QUESTION:
Implement a function `sort_list(arr)` that takes a list of integers as input, sorts the list in ascending order, and preserves the order of duplicate elements. The function should not use any built-in sorting functions or algorithms, have a time complexity of O(n log n), and a space complexity of O(1).
"""

def sort_list(arr):
    def partition(arr, low, high):
        pivot = arr[high]  # choose the last element as the pivot
        i = low - 1  # index of smaller element

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)

            quicksort(arr, low, pivot_index - 1)  # recursively sort the left partition
            quicksort(arr, pivot_index + 1, high)  # recursively sort the right partition

    quicksort(arr, 0, len(arr) - 1)
    return arr