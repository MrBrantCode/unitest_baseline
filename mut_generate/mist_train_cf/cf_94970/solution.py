"""
QUESTION:
Write a function called `reverse_array` that takes an array of integers as input and reverses its elements in-place, without using any built-in functions or creating a new array. The function should have a time complexity of O(n) and use constant extra space. The input array will contain integers ranging from -10^9 to 10^9.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr