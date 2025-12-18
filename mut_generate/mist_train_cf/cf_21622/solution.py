"""
QUESTION:
Create a function named `sum_of_squares` that takes two parameters, `start` and `end`, and returns the sum of the squares of all numbers between them. Both `start` and `end` should be integers and `start` should be less than `end`. If either of these conditions is not met, return an error message.
"""

def sum_of_squares(start, end):
    if type(start) != int or type(end) != int:
        return "Error: The parameters should be integers."
    elif start >= end:
        return "Error: The start parameter should be less than the end parameter."
    else:
        sum_squares = 0
        for i in range(start, end+1):
            sum_squares += i**2
        return sum_squares