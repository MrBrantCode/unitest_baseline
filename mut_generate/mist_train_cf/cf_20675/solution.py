"""
QUESTION:
Write a function named `sum_of_squares` that calculates the sum of the squares of all odd numbers in a given list that are greater than 5. The function should take a list of integers as input and return the sum of squares as output. The function should not modify the original list.
"""

def sum_of_squares(numbers):
    return sum(x**2 for x in numbers if x > 5 and x % 2 == 1)