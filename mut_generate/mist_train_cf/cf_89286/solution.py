"""
QUESTION:
Implement a function called `compute_median` that takes an array of integers as input and returns the median of the array. The function should not use any built-in sorting functions. If the array has an odd number of elements, the median is the middle element. If the array has an even number of elements, the median is the average of the two middle elements.
"""

def compute_median(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
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
    if n % 2 == 0:
        median_index1 = n // 2
        median_index2 = median_index1 - 1
        median1 = quickselect(arr, 0, n - 1, median_index1)
        median2 = quickselect(arr, 0, n - 1, median_index2)
        return (median1 + median2) / 2
    else:
        median_index = n // 2
        return quickselect(arr, 0, n - 1, median_index)