"""
QUESTION:
Write a function `reverse_array` that takes an array and reverses its elements recursively, with a space complexity of O(log N), where N is the number of elements in the array. The function should modify the original array in-place, and its parameters should include the array and two indices representing the start and end of the reversal operation.
"""

def reverse_array(arr, start, end):
    if start >= end:
        return

    arr[start], arr[end] = arr[end], arr[start]
    return reverse_array(arr, start+1, end-1)