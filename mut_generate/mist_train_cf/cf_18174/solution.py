"""
QUESTION:
Implement a function named `find_median` that takes a list of positive integers as input, where the length of the list is an odd number between 1000 and 5000 (inclusive), and the integers are in the range of 1 to 1000. The function should return the median value of the list. The function should not use any built-in sorting functions or data structures, and it should have a time complexity of O(nlogn).
"""

def find_median(arr):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickselect(arr, low, high, k):
        if low == high:
            return arr[low]

        pivot_index = partition(arr, low, high)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)

    n = len(arr)
    return quickselect(arr, 0, n - 1, n // 2)