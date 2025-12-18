"""
QUESTION:
Implement a function `sort_list` that sorts a list of integers in ascending order without using any built-in sorting functions or algorithms. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def sort_list(arr):
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
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    quicksort(arr, 0, len(arr) - 1)
    return arr