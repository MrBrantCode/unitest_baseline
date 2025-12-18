"""
QUESTION:
Write a function called `reverse_array` that takes an array as input, reverses the order of its elements, and returns the reversed array without modifying the original array.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    arr_copy = arr[:]
    while start < end:
        arr_copy[start], arr_copy[end] = arr_copy[end], arr_copy[start]
        start += 1
        end -= 1
    
    return arr_copy