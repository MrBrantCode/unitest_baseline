"""
QUESTION:
Write a recursive function called `calculate_sum` that takes an array of numbers as input and returns the sum of all elements in the array without using any loops or built-in sum functions. The function should be able to handle an empty array as input.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + calculate_sum(arr[1:])