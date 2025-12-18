"""
QUESTION:
Implement the `insertionSort` function that sorts an array of integers (including negative numbers and zeroes) using the insertion sort algorithm and returns the sorted array along with the total number of shifts made during the sorting process. A shift is defined as moving a number to make space for inserting another number in its correct place.
"""

def insertionSort(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        arr[j + 1] = key
    return arr, shifts