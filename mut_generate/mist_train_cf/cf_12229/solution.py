"""
QUESTION:
Create a function named `insertion_sort` that takes an array of numbers as input and returns the array sorted in ascending order. The array can contain duplicate numbers and its length should be at least 10.
"""

def entrance(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr