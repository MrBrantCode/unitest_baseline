"""
QUESTION:
Write a function called `reverse_array` that takes an array of integers as input and reverses the array in place, without using any built-in methods or functions that directly reverse the array. The function should have a time complexity of O(n), where n is the length of the array.
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr