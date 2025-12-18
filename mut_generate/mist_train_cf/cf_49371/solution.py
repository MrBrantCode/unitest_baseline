"""
QUESTION:
Construct a function named `multiply_by_two` that takes an array of unique integers as input and returns a new array where each element is the result of multiplying the corresponding element in the input array by two.
"""

def multiply_by_two(arr):
    # Create a new list comprehension that multiplies each element by two
    return [i * 2 for i in arr]