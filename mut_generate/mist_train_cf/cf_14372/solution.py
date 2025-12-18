"""
QUESTION:
Create a function named `check_number` that takes an integer as input and returns a string describing whether the number is "Even and Positive", "Even", "Positive", or "Neither Even nor Positive" using nested ternary operators and helper functions `is_even` and `is_positive`.
"""

def check_number(number):
    return "Even and Positive" if number % 2 == 0 and number > 0 else \
           "Even" if number % 2 == 0 else \
           "Positive" if number > 0 else \
           "Neither Even nor Positive"