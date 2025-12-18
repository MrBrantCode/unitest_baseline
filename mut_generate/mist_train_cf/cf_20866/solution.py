"""
QUESTION:
Write a function named `reverse_array` that takes one argument `arr` representing an array of integers, reverses the order of its elements in-place, and returns the modified array. The function should not use any built-in reverse or sort functions and have a time complexity of O(n), where n is the length of the input array. The input array will always contain at least 10 elements and at most 1000 elements.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr