"""
QUESTION:
Write a function named 'add_values' that takes two parameters x and y where x is an integer and y is a string representing an integer. The function should return the sum of x and y without changing their original data types. Note that x and y should be converted to the same data type before performing the addition operation.
"""

def add_values(x, y):
    return x + int(y)