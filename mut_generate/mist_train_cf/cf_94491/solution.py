"""
QUESTION:
Implement a function called `reorderArray` that takes in an array of integers as input and returns the array with the numbers rearranged in descending order. The function should have a time complexity of O(n log n), where n is the length of the input array, and should not use any additional data structures or built-in sorting algorithms.
"""

def reorderArray(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            quicksort(arr, low, pivot - 1)
            quicksort(arr, pivot + 1, high)

    quicksort(arr, 0, len(arr) - 1)
    return arr