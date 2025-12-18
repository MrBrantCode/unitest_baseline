"""
QUESTION:
Create a function `mathematical_function` that takes two string parameters `x` and `y`, where `x` is a binary number and `y` is a hexadecimal number. The function should convert these strings to base 10 integers, then calculate the result of `x^3 + 2*y^2`. If either `x` or `y` is not a valid number in its respective base, the function should return an error message.
"""

def entance(x, y):
    try:
        x = int(x, 2)
        y = int(y, 16)
        return x**3 + 2*(y**2)
    except (TypeError, ValueError):
        return "Error: Invalid input. Please enter a valid string representing a number in the base."