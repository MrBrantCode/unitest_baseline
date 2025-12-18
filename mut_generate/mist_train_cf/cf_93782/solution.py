"""
QUESTION:
Implement a function `insertion_sort_descending` that sorts an array of integers in descending order using the insertion sort algorithm. The array has at least 2 and at most 10^5 unique elements ranging from -10^9 to 10^9. The function should use an in-place approach without additional data structures.
"""

def insertion_sort_descending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr