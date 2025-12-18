"""
QUESTION:
Write a function `sort_array_descending(arr)` that takes an array of integers as input, sorts the array in descending order, and returns the sorted array. The function must have a time complexity of O(n^2) and cannot use any built-in sorting functions or data structures. The function should also handle duplicate integers in the array and ensure that they are placed adjacent to each other in the sorted array.
"""

def sort_array_descending(arr):
    n = len(arr)
    for i in range(n-1):
        current_max = arr[i]
        max_index = i
        for j in range(i+1, n):
            if arr[j] > current_max:
                current_max = arr[j]
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr