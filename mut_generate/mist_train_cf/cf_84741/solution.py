"""
QUESTION:
Implement the quicksort function with a modification to handle duplicate elements efficiently. The function should take an array as input and return the sorted array. You are required to use the "Median of three quicksort" variation, which chooses the pivot as the median of the array[start], array[center], and array[end] and swaps it with array[end].
"""

def quicksort(arr):
    _quicksort_helper(arr, 0, len(arr) - 1)
    return arr

def _quicksort_helper(arr, left, right):
    if left < right:
        _choose_pivot(arr, left, right)
        pivot_index = _partition(arr, left, right)
        _quicksort_helper(arr, left, pivot_index - 1)
        _quicksort_helper(arr, pivot_index + 1, right)

def _choose_pivot(arr, left, right):
    mid = left + (right - left) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    arr[mid], arr[right] = arr[right], arr[mid]

def _partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1