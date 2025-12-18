"""
QUESTION:
Implement a function called `insertion_sort_recursive` that takes an array `arr` and the number of elements `n` as parameters. The function should sort the array in ascending order using the insertion sort algorithm in a recursive manner without using any built-in sorting functions or methods. The function should not return any value, but instead sort the array in-place.
"""

def insertion_sort_recursive(arr, n):
    # Base case: If array has only one element, it is already sorted
    if n <= 1:
        return
    
    # Sort first n-1 elements
    insertion_sort_recursive(arr, n-1)
    
    # Insert the last element at its correct position in the sorted subarray
    key = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key