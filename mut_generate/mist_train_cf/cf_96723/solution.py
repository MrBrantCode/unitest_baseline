"""
QUESTION:
Write a function named `reverse_array` that takes an array of integers as input and reverses its elements in-place, without using any additional data structures. The function should have a time complexity of O(n), where n is the length of the array, and a space complexity of O(1).
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr