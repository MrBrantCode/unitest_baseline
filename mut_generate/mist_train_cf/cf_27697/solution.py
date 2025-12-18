"""
QUESTION:
Implement a function named `sum_of_squares_of_even_numbers` that takes a list of integers as input and returns the sum of the squares of all the even numbers in the list. The function should return 0 if the input list is empty or does not contain any even numbers. Use the numpy library for array operations.
"""

import numpy as np

def sum_of_squares_of_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if not even_numbers:
        return 0
    even_numbers_array = np.array(even_numbers)
    sum_of_squares = np.sum(even_numbers_array ** 2)
    return sum_of_squares