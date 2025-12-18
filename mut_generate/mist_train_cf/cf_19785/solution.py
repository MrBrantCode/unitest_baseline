"""
QUESTION:
Implement a function named `bubble_sort_descending` that sorts an array of integers in descending order without using any built-in sorting functions or data structures. The function should have a time complexity of O(n^2).
"""

def bubble_sort_descending(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        n -= 1

    return arr