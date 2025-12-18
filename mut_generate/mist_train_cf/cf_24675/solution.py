"""
QUESTION:
Write a function named `recursive_sum` that takes an array as input and returns the sum of all its elements using a recursive approach. The function should only take one argument (the array) and should not use any loops.
"""

def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])