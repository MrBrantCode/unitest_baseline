"""
QUESTION:
Implement the function `sort_list(arr)` to sort a list of integers in non-decreasing order (smallest to largest) without using any built-in sorting functions or algorithms. The function should have a time complexity of O(n log n) and a space complexity of O(1), and it should preserve the order of duplicate elements in the input list.
"""

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


def sort_list(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr