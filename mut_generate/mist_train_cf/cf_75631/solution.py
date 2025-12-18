"""
QUESTION:
Write a function called `reverse_arr` that takes an array `arr` as input and reverses it in-place. The function should handle cases where the input array contains duplicate and/or negative values. The function should not use any built-in reverse functions.
"""

def reverse_arr(arr):
    """Reverses an array in-place. This means the existing array will be modified!
    The function should handle cases where the input array contains duplicate and/or negative values."""
    
    # Step 1: Create pointers for the start and end of the array
    start = 0
    end = len(arr) - 1
      
    # Step 2: Implement a loop that swaps the values at the start and end pointers
    # and gradually moves the pointers towards each other until they meet or surpass each other.
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    # Step 3: Return the reversed array
    return arr