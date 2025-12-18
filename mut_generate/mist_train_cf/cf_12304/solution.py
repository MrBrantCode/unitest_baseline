"""
QUESTION:
Write a function named `reverseArray(arr, start, end)` that takes an array and two indices as parameters. The function should reverse the elements of the array in-place, without using any loops or built-in array manipulation functions, and without creating a new array. The time complexity of the function should be considered O(1) despite the use of recursion.
"""

def reverseArray(arr, start, end):
    if start >= end:
        return
    # Swap elements at start and end indices
    arr[start], arr[end] = arr[end], arr[start]
    # Recursive call with updated start and end indices
    reverseArray(arr, start + 1, end - 1)