"""
QUESTION:
Create a function named `sortDescending` that takes an array of integers as input and returns the sorted array in descending order. The function should sort the array in-place, meaning it should not create a new array, but instead modify the original array.
"""

def sortDescending(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr