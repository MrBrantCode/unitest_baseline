"""
QUESTION:
Write a function called `reverse_list` that takes a list as input and reverses it in-place without using any predefined functions. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def reverse_list(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start += 1
        end -= 1
    
    return arr