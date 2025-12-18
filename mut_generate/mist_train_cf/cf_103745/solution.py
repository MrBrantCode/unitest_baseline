"""
QUESTION:
Write a function named `find_maximum` that takes an array of integers as input and returns the maximum value in the array. The function should not use any built-in functions to find the maximum value. The time complexity of the function should be O(n) and the space complexity should be O(1), where n is the number of elements in the array.
"""

def find_maximum(arr):
    if len(arr) == 0:
        return None

    max_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value