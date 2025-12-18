"""
QUESTION:
Create a function sum_of_squares that calculates the sum of squares of a list of numbers in both Python and Cython, and compare the performance of the two languages. The function should take a list of integers as input and return the sum of squares as output. Note that Cython code requires explicit memory management using C-style memory allocation and deallocation.
"""

def sum_of_squares(numbers):
    result = 0
    for num in numbers:
        result += num**2
    return result