"""
QUESTION:
Implement the `insertion_sort_descending_length` function to sort a list of strings in descending order based on the length of each string. The function should take a list of strings as input and return the sorted list. The function should use the insertion sort algorithm and should not use any built-in sorting functions.
"""

def insertion_sort_descending_length(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(arr[j]) < len(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr