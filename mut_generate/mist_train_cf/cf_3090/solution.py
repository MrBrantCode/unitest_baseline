"""
QUESTION:
Implement the `reverse_and_sort_array` function to reverse a given array of numbers in-place and sort it in ascending order. The function should not use any built-in methods or additional data structures and should have a time complexity less than O(n^2).
"""

def reverse_and_sort_array(arr):
    def quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort(arr, low, pivot_index - 1)
            quick_sort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    quick_sort(arr, 0, len(arr) - 1)