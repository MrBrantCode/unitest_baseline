"""
QUESTION:
Implement a function named `quick_sort` that takes a list of integers as input and returns the sorted list using the QuickSort algorithm. Ensure the function works in-place and uses the Hoare Partition scheme with the middle element as the pivot.
"""

def quick_sort(arr):
    def partition(arr, low, high):
        pivot_index = (low + high) // 2
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort_helper(arr, low, pivot_index - 1)
            quick_sort_helper(arr, pivot_index + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)