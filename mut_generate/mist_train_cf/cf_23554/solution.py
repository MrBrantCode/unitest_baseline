"""
QUESTION:
Write a function `sum_of_even_squares` that calculates the sum of the squares of all even numbers in a given array of integers. The function should take one parameter, an array of integers, and return the sum of squares of even numbers.
"""

def sum_of_even_squares(array):
    return sum([x**2 for x in array if x % 2 == 0])