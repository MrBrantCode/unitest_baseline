"""
QUESTION:
Create a function named `check_number` that takes one input. The function should accept any numerical input, determine whether the number is negative, positive, or zero, and return a corresponding message. If the input is non-numerical, the function should return an error message.
"""

def entrance(num):
    try:
        num = float(num)
        if num > 0:
            return "The number is positive."
        elif num < 0:
            return "The number is negative."
        else:
            return "The number is zero."
    except ValueError:
        return "Invalid input, please enter a numerical input."