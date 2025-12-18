"""
QUESTION:
Implement the function `find_median` to find the median of a list of integers. The list will always contain an odd number of elements. The function should have a time complexity of O(n log n) and should not use any built-in sorting functions or libraries. The function should also not use any additional space beyond the input list. The input list will be modified in-place.
"""

def find_median(arr):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
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