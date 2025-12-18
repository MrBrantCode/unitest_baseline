"""
QUESTION:
Implement a function named `sort_array_descending` that sorts a given linear array in descending order using a variation of quicksort. The function should sort the array in-place without using any additional data structures, with a time complexity of O(nlogn) and a space complexity of O(logn), and correctly handle arrays containing duplicate elements.
"""

def partition(arr, low, high):
    """Selects the last element as the pivot and rearranges the array such that all elements greater than or equal to the pivot are placed to its left and all elements smaller than the pivot are placed to its right."""
    pivot = arr[high]  
    i = low - 1  

    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    """Recursively applies the partitioning step to the left and right subarrays."""
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def sort_array_descending(arr):
    """Sorts a given linear array in descending order using a variation of quicksort."""
    quicksort(arr, 0, len(arr) - 1)