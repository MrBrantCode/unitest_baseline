"""
QUESTION:
Design a function named `find_median` that takes an array of n integers as input, where n is an odd number greater than 1, and returns the median of the array. The function should not use any built-in sorting functions or data structures, and it should achieve a time complexity of O(n) and a space complexity of O(n).
"""

def find_median(arr):
    # Helper function to swap elements in the array
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    # Helper function to partition the array
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                swap(arr, i, j)

        swap(arr, i + 1, high)
        return i + 1

    # Helper function to find the median
    def find_median_helper(arr, low, high, target_index):
        if low == high:
            return arr[low]

        pivot_index = partition(arr, low, high)
        if target_index == pivot_index:
            return arr[pivot_index]
        elif target_index < pivot_index:
            return find_median_helper(arr, low, pivot_index - 1, target_index)
        else:
            return find_median_helper(arr, pivot_index + 1, high, target_index)

    n = len(arr)
    median_index = n // 2
    return find_median_helper(arr, 0, n - 1, median_index)