"""
QUESTION:
Create a function called `insertion_sort_reverse` that takes an array of integers as input and sorts the array in descending order using the insertion sort algorithm. The integers in the array can range from -10^6 to 10^6 and the length of the array is between 10^3 and 10^6.
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