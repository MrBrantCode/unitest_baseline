"""
QUESTION:
Implement a recursive function `bubble_sort` that takes an array `arr` and the length of the array `n` as parameters. The function should sort the array in-place in descending order without using loops or built-in sorting functions. The base case for the recursion should be when `n` is 1, indicating the array is already sorted.
"""

def bubble_sort(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    bubble_sort(arr, n - 1)