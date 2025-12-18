"""
QUESTION:
Write a function named `compute_median` that computes the median of a set of integers without using any built-in sorting functions. The function should handle cases where the set has an odd or even number of elements.
"""

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

def compute_median(arr):
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