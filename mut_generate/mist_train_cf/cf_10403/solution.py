"""
QUESTION:
Implement a function named `bubble_sort` that sorts an array of integers in ascending order without using the built-in sort() function. The function should take an array of integers as input and return the sorted array. The implementation should not use explicit loops or recursion, although internal loops within the algorithm are allowed.
"""

def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True

    return arr