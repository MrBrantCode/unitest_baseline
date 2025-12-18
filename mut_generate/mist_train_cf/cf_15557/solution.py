"""
QUESTION:
Implement the `insertion_sort_descending` function to sort an array of integers in descending order using an in-place insertion sort algorithm. The input array contains at least 2 and at most 10^5 unique integers ranging from -10^9 to 10^9.
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