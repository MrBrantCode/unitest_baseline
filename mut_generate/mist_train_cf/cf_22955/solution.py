"""
QUESTION:
Write a function `reverse_array` that reverses the order of numbers in a given array without using any additional data structures, with a time complexity of O(n), where n is the length of the array. The function should only modify the original array.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr