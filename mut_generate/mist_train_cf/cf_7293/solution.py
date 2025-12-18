"""
QUESTION:
Write a function `reverse_array` that takes an array as input and reverses its order using a recursive approach without using any built-in reverse functions or temporary variables. The function should modify the original array in-place and return the reversed array.
"""

def reverse_array(arr):
    def reverse_helper(arr, start, end):
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        reverse_helper(arr, start + 1, end - 1)
    
    reverse_helper(arr, 0, len(arr) - 1)
    return arr