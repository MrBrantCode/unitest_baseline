"""
QUESTION:
Write a function `find_max_value` that takes an array of integers as input and returns the maximum value in the array. The function should have a time complexity of O(n), where n is the length of the array.
"""

def find_max_value(arr):
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value