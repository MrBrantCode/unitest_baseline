"""
QUESTION:
Create a function `add_numbers` that takes two positive integers as input and returns their sum. Both integers must be less than 1000. If the inputs are invalid, return an error message.
"""

def add_numbers(a, b):
    if a < 0 or b < 0:
        return "Numbers must be positive integers."
    elif a >= 1000 or b >= 1000:
        return "Numbers must be less than 1000."
    else:
        return a + b