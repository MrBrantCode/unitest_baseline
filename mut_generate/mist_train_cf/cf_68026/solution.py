"""
QUESTION:
Write a function `reverse_array(arr)` that reverses the order of the input array `arr` without using any predefined or built-in methods, such as `reverse()` or `reversed()`. The function should take an array as input and return the reversed array.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr