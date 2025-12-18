"""
QUESTION:
Create a Python function named `square_number` that takes one argument, `number`. The function should return the square of the number if it is positive (greater than 0), less than or equal to 10, and even. Otherwise, if the number is odd, return the negative of the number squared.
"""

def square_number(number):
    return number ** 2 if number > 0 and number <= 10 and number % 2 == 0 else -(number ** 2)