"""
QUESTION:
Define a function named `square_array` that takes an array of integers as input and returns a new array containing the squares of the input values as positive numbers. The function should handle both positive and negative input values.
"""

def square_array(arr):
    return [abs(num ** 2) for num in arr]