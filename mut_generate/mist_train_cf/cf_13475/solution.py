"""
QUESTION:
Write a function named `square` that takes an iterable of numbers as input and returns a list of their squares. The function should be implemented as a one-liner lambda function and utilize the `map()` function.
"""

def square(x):
    """Returns a list of squares of input numbers"""
    return list(map(lambda i: i * i, x))