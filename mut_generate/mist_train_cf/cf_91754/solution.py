"""
QUESTION:
Write a recursive function `calculate_sum` that calculates the sum of all elements in a given array of numbers without using any loops or built-in sum functions. The function should take an array of numbers as input and return the sum of its elements.
"""

def calculate_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + calculate_sum(arr[1:])