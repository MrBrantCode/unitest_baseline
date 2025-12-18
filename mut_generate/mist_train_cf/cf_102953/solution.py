"""
QUESTION:
Create a function called `insertion_sort` that sorts an array of integers using the insertion sort algorithm and returns the number of comparisons made during the sorting process. The function should take an array as input, sort it in ascending order, and keep track of the number of comparisons made. The array should be modified in-place, meaning that the original array is sorted instead of creating a new sorted array.
"""

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons