"""
QUESTION:
Implement a function `selection_sort_descending(arr)` that takes an array of integers as input, sorts it in descending order using a modified selection sort algorithm, and returns the sorted array. The array may contain duplicate elements. The function should have a time complexity of O(n^2) and should be able to handle arrays of any size.
"""

def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] >= arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr