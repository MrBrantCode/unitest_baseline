"""
QUESTION:
Write a function called `add_numbers` that takes a list of numbers as input and returns their sum using a lambda expression and the `reduce` function. The input list will contain at least two numbers. The solution should import the necessary modules and use a lambda function to perform the addition operation.
"""

from functools import reduce

def add_numbers(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total