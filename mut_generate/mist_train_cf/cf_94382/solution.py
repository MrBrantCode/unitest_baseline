"""
QUESTION:
Implement a function `quick_sort(arr)` that sorts an array of integers in ascending order using the quick sort algorithm with the Lomuto partition scheme. The function should handle arrays of any size, including empty arrays and arrays with duplicate elements, without using any built-in sorting functions or libraries.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # Select the last element as the pivot
    i = 0  # Index to track the position of the pivot

    for j in range(len(arr)-1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[-1] = arr[-1], arr[i]  # Move pivot to its correct position

    left = quick_sort(arr[:i])
    right = quick_sort(arr[i+1:])

    return left + [arr[i]] + right