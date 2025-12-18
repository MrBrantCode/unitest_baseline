"""
QUESTION:
Create a function `check_number` that takes one integer argument and returns a string indicating whether the number is even, positive, both, or neither. The function must use nested ternary operators and user-defined functions within the conditionals to evaluate the number's parity and sign.
"""

def is_even(number):
    return number % 2 == 0

def is_positive(number):
    return number > 0

def check_number(number):
    result = "Even and Positive" if is_even(number) and is_positive(number) else \
             "Even" if is_even(number) else \
             "Positive" if is_positive(number) else \
             "Neither Even nor Positive"
    
    return result