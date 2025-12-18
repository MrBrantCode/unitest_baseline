"""
QUESTION:
Write a function named `reverse_and_sort_array` that takes an array of integers as input. The function should reverse the input array in-place and sort it in ascending order without using any built-in methods or additional data structures. The time complexity of the function should be less than O(n^2).
"""

def reverse_and_sort_array(arr):
    start = 0
    end = len(arr) - 1

    # Reverse the array in-place
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    # Sort the reversed array using Quick Sort
    def quick_sort(arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = partition(arr, low, high)

            # Recursively apply quick sort to the left and right sub-arrays
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

    quick_sort(arr, 0, len(arr) - 1)