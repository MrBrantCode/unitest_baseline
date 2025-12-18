"""
QUESTION:
Implement a function `reverse_array(arr)` that takes an array of integers as input and reverses it in-place with a time complexity of O(n) and a space complexity of O(1). The array can contain up to 10^6 integers, each ranging from 1 to 10^9 (inclusive).
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap the elements at start and end indices
        arr[start], arr[end] = arr[end], arr[start]

        # Move the pointers towards each other
        start += 1
        end -= 1

    return arr