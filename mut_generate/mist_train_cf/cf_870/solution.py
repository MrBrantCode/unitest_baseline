"""
QUESTION:
Create a function named `reverse_array` that takes one argument, an array that can contain integers, strings, and nested arrays. The function should reverse the elements of the input array in-place without using any built-in array reverse function or any additional array or data structure. The function should also recursively reverse any nested arrays.
"""

def reverse_array(arr):
    def reverse(start, end):
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        reverse(start + 1, end - 1)

    def reverse_helper(arr):
        if isinstance(arr, list):
            reverse(0, len(arr) - 1)
            for i in range(len(arr)):
                arr[i] = reverse_helper(arr[i])
        return arr

    return reverse_helper(arr)