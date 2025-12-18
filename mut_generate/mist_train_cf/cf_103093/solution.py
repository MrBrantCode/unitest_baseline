"""
QUESTION:
Create a function `sum_of_squares` that calculates the sum of squares of a list of numbers, where each number is raised to the power of a given exponent. The function should take two parameters: a list of numbers and the exponent, and return the total sum.
"""

def sum_of_squares(numbers, exponent):
    sum = 0
    for num in numbers:
        sum += num ** exponent
    return sum