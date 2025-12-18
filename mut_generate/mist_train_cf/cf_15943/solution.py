"""
QUESTION:
Construct a function named `is_multiple_of_three_or_five` that takes an integer as input and returns a boolean value. The function should return True if the number is a multiple of 3 or a multiple of 5, but not both, and also consider the case when the number is zero.
"""

def is_multiple_of_three_or_five(number):
    return ((number % 3 == 0) or (number % 5 == 0)) and not ((number % 3 == 0) and (number % 5 == 0)) or (number == 0)