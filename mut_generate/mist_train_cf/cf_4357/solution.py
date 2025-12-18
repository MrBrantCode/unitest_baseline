"""
QUESTION:
Create a function named `reverse_array` that takes an array `arr` as input, clones it, reverses the order of its elements, and returns the reversed array. The original array should remain unchanged. The function must be implemented using recursion and should not use any built-in array manipulation functions such as reverse or slice.
"""

def reverse_array(arr):
    if len(arr) == 0:
        return []
    else:
        return [arr[-1]] + reverse_array(arr[:-1])