"""
QUESTION:
Design a function named `find_median` that takes a large array of integers as input and returns the median value(s). The function should have a time complexity of O(n) or better and should not use any built-in sorting functions or libraries. If there are multiple medians (i.e., the array size is even), the function should return both values.
"""

def find_median(arr):
    n = len(arr)
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
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

    if n % 2 == 0:
        median1 = quickselect(0, n - 1, n // 2)
        median2 = quickselect(0, n - 1, n // 2 - 1)
        if median1 == median2:
            return median1
        else:
            return [median1, median2]
    else:
        return quickselect(0, n - 1, n // 2)