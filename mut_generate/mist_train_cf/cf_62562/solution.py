"""
QUESTION:
Write a function named `sort_in_place(arr)` that takes an array of integers as input and returns the sorted array in ascending order. The function must sort the array in-place, meaning it should not create a new array, but instead modify the original array.
"""

def sort_in_place(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr