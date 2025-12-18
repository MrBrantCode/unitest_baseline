"""
QUESTION:
Write a function `sort_list` that takes a list of integers as input and sorts the list in ascending order without using any built-in sorting functions or algorithms. The function should have a time complexity of O(n log n) and a space complexity of O(1).
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

def sort_list(arr):
    def quicksort(low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort(low, pi - 1)
            quicksort(pi + 1, high)

    quicksort(0, len(arr) - 1)