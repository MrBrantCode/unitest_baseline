"""
QUESTION:
Implement a function `reverse_array(start, end)` to reverse a given array in a recursive manner. The function should not use any built-in array reverse methods and should have a time complexity of O(n) and a space complexity of O(1).
"""

def reverse_array(start, end, arr):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(start + 1, end - 1, arr)