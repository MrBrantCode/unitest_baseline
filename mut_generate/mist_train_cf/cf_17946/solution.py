"""
QUESTION:
Write a function named `reverse_array` that takes an array of integers as input and reverses the order of its elements in-place, without using any built-in functions or creating a new array. The function should have a time complexity of O(n) and should not use any extra space beyond a few integer variables.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr