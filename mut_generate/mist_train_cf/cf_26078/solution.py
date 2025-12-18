"""
QUESTION:
Create a function `cubes_of_numbers` that returns a list of cubes of the first n natural numbers. The function should take an integer n as input and return a list of cubes of numbers from 1 to n. In this case, n is 10.
"""

def cubes_of_numbers(n):
    """Returns a list of cubes of the first n natural numbers."""
    return [i ** 3 for i in range(1, n + 1)]