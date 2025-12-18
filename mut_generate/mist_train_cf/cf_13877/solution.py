"""
QUESTION:
Implement a function named `reverse_array` that reverses the elements of the input array in-place without using any additional data structures. The function should modify the original array and return it. The input array will contain elements of any data type.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr