"""
QUESTION:
Implement a function named `find_median` to compute the median of an array containing floating-point numbers without using the built-in `sorted()` function or any external libraries. The array may contain up to 1 million elements, may include duplicates, and the time complexity of the solution should be O(n log n). The function should return the median rounded to the nearest integer.
"""

def find_median(arr):
    n = len(arr)
    if n % 2 == 0:
        k1 = n // 2
        k2 = k1 - 1
        median = (find_kth_smallest(arr, k1) + find_kth_smallest(arr, k2)) / 2
    else:
        k = n // 2
        median = find_kth_smallest(arr, k)
    return round(median)

def find_kth_smallest(arr, k):
    left = 0
    right = len(arr) - 1
    while True:
        pivot_index = partition(arr, left, right)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            right = pivot_index - 1
        else:
            left = pivot_index + 1

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1