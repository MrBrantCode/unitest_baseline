"""
QUESTION:
Write a function named `reverse_array` that takes an array as input and reverses its order without using any built-in reverse or sorting functions. The function should modify the original array and return it.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap elements at start and end pointers
        arr[start], arr[end] = arr[end], arr[start]

        # Move pointers
        start += 1
        end -= 1

    return arr