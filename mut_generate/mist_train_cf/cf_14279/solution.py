"""
QUESTION:
Implement a function called `insertion_sort_descending_length` that sorts a list of strings in descending order based on the length of each string using the insertion sort algorithm. The function should take a list of strings as input and return the sorted list.
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