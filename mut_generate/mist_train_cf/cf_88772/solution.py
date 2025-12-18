"""
QUESTION:
Create a function named `sort_array_descending` that sorts an array of integers in descending order without using any built-in sorting functions or data structures. The function should have a time complexity of O(n^2) and handle duplicate integers by placing them adjacent to each other in the sorted array.
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