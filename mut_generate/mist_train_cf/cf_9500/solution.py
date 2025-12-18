"""
QUESTION:
Create a function named `reverse_array` that takes an array as input and reverses its elements in-place without using any built-in array reverse functions or additional data structures.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        # Swap elements
        arr[start], arr[end] = arr[end], arr[start]
        
        # Move towards the middle
        start += 1
        end -= 1
    
    return arr