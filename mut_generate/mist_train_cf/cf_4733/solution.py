"""
QUESTION:
Create a function named `reverse_array` that takes an array as input and reverses the order of its elements in-place, without using any built-in array reversal methods, additional memory allocation, recursion, or temporary variables. The function should return the modified array.
"""

def reverse_array(array):
    start = 0
    end = len(array) - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    return array