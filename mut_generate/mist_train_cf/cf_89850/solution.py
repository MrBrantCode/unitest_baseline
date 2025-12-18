"""
QUESTION:
Create a function named `reverse_array` that takes an array as input and reverses its order without using any built-in reverse functions or temporary variables. The function should use a recursive approach. The input array is not empty and consists of elements that can be swapped.
"""

def reverse_array(arr):
    def reverse_helper(arr, start, end):
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        reverse_helper(arr, start + 1, end - 1)
    
    reverse_helper(arr, 0, len(arr) - 1)
    return arr