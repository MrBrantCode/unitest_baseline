"""
QUESTION:
Implement a function `bubble_sort_descending` that sorts an array of integers in descending order without using any built-in sorting functions or libraries. The array can contain duplicate elements, has a length of at most 10^6, and its elements are integers between -10^9 and 10^9.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr