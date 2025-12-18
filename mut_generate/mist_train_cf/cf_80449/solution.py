"""
QUESTION:
Implement a function named `insertion_sort_recursive` that uses recursion to sort an array of n distinct numerical values, which can be integers or floating point numbers, using the insertion sort technique. The function should take an array `arr` and its length `n` as input and modify the array in-place to be sorted in ascending order.
"""

def insertion_sort_recursive(arr, n):
    # base case
    if n <= 1:
        return

    # Sort first n-1 elements
    insertion_sort_recursive(arr, n-1)

    # Insert last element at its correct position in sorted array.
    last = arr[n-1]
    j = n-2

    # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
    while (j >= 0 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1] = last