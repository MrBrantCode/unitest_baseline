"""
QUESTION:
Write a function named `sum_of_squares` that calculates the sum of squares of a list of numbers using Cython and compare its performance to the equivalent function in Python. The function should take a list of integers as input and return the sum of their squares. Use Cython's explicit memory management to optimize the function.
"""

def sum_of_squares(numbers):
    result = 0
    for num in numbers:
        result += num**2
    return result