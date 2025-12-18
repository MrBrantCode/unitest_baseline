"""
QUESTION:
Write a function `find_median(arr)` that takes a list of integers `arr` with an odd number of elements as input and returns the median of the list. The function should have a time complexity of O(n log n) and should not use any built-in sorting functions or libraries. The function should also not use any additional space beyond the input list.
"""

def find_median(arr):
    n = len(arr)

    def partition(low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickselect(low, high, k):
        if low == high:
            return arr[low]

        pivot_index = partition(low, high)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(low, pivot_index - 1, k)
        else:
            return quickselect(pivot_index + 1, high, k)

    return quickselect(0, n - 1, n // 2)