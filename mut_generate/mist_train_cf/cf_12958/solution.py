"""
QUESTION:
Write a function named `reverse_list` that takes a list as input and reverses it in-place without using any predefined list reversal functions. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def reverse_list(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        # Swap elements at start and end pointers
        arr[start], arr[end] = arr[end], arr[start]
        
        # Increment start and decrement end
        start += 1
        end -= 1
    
    return arr