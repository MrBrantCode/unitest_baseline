"""
QUESTION:
Write a function named `reverse_array` that takes an array of integers as input, reverses it in place without using any built-in reversing functions or methods, and returns the reversed array. The function should have a time complexity of O(n), where n is the length of the array.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        # Swap the elements at start and end indices
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr