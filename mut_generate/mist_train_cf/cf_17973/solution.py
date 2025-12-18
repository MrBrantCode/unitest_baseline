"""
QUESTION:
Implement a function named `reverse_array` that takes an array as input, reverses it in place without using any built-in functions or libraries that directly reverse the array, and returns the reversed array. The solution should have a time complexity of O(n), where n is the length of the array, and should handle arrays with duplicates efficiently without using any additional space.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr