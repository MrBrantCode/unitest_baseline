"""
QUESTION:
Write a function `insertion_sort_reverse` that sorts a list of integers in reverse order using the insertion sort algorithm. The list can contain integers ranging from -10^6 to 10^6 and its length can be between 10^3 and 10^6. The function should return the sorted list.
"""

def insertion_sort_reverse(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr