"""
QUESTION:
Implement a function `reverse_array(arr)` that takes an array of integers as input and reverses the array in-place. The array has a maximum size of 10^9 and its elements are integers between 1 and 10^9 (inclusive). The function should have a time complexity of O(n) and a space complexity of O(1), and it should not use any built-in functions or methods that directly reverse the array.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr