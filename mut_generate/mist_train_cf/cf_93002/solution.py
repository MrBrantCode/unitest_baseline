"""
QUESTION:
Create a function called `reverse_array` that takes an array `arr` as input, reverses its elements in-place without using any additional data structures, and returns the reversed array. The function should only use the input array for swapping elements and not create any additional arrays or data structures.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr