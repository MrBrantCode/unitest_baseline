"""
QUESTION:
Implement a function `find_median(arr)` that takes a list of 1000 to 5000 unique or duplicate positive integers (ranging from 1 to 1000) as input and returns the median value. The list is not sorted. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions or data structures.
"""

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

def find_median(arr):
    n = len(arr)
    if n % 2 == 0:
        mid1 = quickselect(arr, 0, n - 1, n // 2 - 1)
        mid2 = quickselect(arr, 0, n - 1, n // 2)
        return (mid1 + mid2) / 2
    else:
        return quickselect(arr, 0, n - 1, n // 2)