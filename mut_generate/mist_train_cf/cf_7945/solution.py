"""
QUESTION:
Implement a function named `sort` that sorts a given list of integers in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(1), and it should not use any built-in sorting functions or libraries. The function should also be an in-place sorting algorithm, meaning it should modify the original list without using any additional data structures.
"""

def sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    quicksort(arr, 0, len(arr) - 1)