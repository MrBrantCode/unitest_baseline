"""
QUESTION:
Implement a function named `reverse_array(arr)` that takes an array `arr` as input, reverses it in-place, and returns the reversed array. The solution should have a time complexity of O(n) and should not use any built-in functions or libraries that directly reverse the array.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr