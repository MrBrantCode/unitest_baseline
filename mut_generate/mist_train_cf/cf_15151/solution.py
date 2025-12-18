"""
QUESTION:
Implement a function named `insertion_sort` that sorts an array of integers in ascending order. The array can contain duplicate elements, and the function should have a time complexity of O(n^2). The function should take a list of integers as input and return the sorted list.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr