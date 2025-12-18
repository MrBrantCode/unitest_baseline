"""
QUESTION:
Write a function named `reverse_array` that takes an array of integers as input and returns the array with its elements in reverse order. The input array will contain between 5 and 100 elements. Do not use any built-in array reversal functions or libraries.
"""

def reverse_array(arr):
    # Initialize two pointers: one at the beginning and one at the end of the array
    start = 0
    end = len(arr) - 1

    # Swap elements until the pointers meet in the middle
    while start < end:
        # Swap the elements at the two pointers
        arr[start], arr[end] = arr[end], arr[start]

        # Move the pointers towards each other
        start += 1
        end -= 1

    return arr