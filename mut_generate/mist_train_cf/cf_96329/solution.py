"""
QUESTION:
Write a function `reverse_array(arr)` that takes an array of at least 10 elements and at most 1000 elements as input and returns the reversed array. The solution should not use any built-in functions or libraries and should have a time complexity of O(n), where n is the length of the input array.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr