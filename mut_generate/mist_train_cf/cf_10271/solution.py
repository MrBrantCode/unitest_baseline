"""
QUESTION:
Write a function named `flatten_and_multiply` that takes a 2D array as input and returns a 1D array where each element is twice the value of the corresponding element in the input array. The function should work with any 2D array containing integers.
"""

def flatten_and_multiply(array):
    return [item*2 for sublist in array for item in sublist]