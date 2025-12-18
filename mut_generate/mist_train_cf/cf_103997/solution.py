"""
QUESTION:
Implement a function named `bubble_sort` that takes an array of integers as input and returns the sorted array. The array should contain positive integers only and have a length between 5 and 1000 (inclusive). The function should use a single outer loop and have a time complexity of O(n^2), where n is the length of the array.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr