"""
QUESTION:
Implement the function `insertion_sort(arr)` that sorts the input array in ascending order using the Insertion Sort algorithm with a single loop and no additional data structures.
"""

def insertion_sort(arr):
    arr_length = len(arr)
    key = arr[1]
    j = 0
    i = 1
    while i < arr_length:
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        i += 1
        if i < arr_length:
            key = arr[i]
    return arr