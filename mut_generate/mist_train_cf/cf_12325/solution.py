"""
QUESTION:
Implement a function called `selection_sort_descending` that sorts a given array of integers in descending order using a modified version of the selection sort algorithm. The array may contain duplicate elements.
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