"""
QUESTION:
Write a function named `square_numbers` that uses a lambda function in combination with the `map` function to square each number in a given list. The function should take a list of integers as input and return a list of their squares. Note that the function should be implemented in Python 3, where the `map` function returns an iterable object of type `map`, not a list or tuple.
"""

def square_numbers(numbers):
    """Returns a list of squares of the given numbers."""
    return list(map(lambda x: x**2, numbers))