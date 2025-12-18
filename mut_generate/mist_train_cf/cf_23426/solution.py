"""
QUESTION:
Write a function named `sum_of_squares` that takes a list of integers as input and returns the sum of the squares of these integers.
"""

def sum_of_squares(numbers):
    sum = 0
    for number in numbers:
        sum += number ** 2
    return sum