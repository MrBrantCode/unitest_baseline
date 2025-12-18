"""
QUESTION:
Write a function `add_two_numbers(a, b)` that takes two parameters `a` and `b` and returns their sum. The function should handle potential errors by checking the data types of `a` and `b` before attempting to add them. The function should be able to handle any data types that support the addition operation in Python.
"""

def add_two_numbers(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Both inputs must be of the same data type that supports addition."