"""
QUESTION:
Write a function `cube_value` that takes a quantifiable input value and returns its cubed outcome. The input value should be either an integer or a floating-point number. If the input value is not quantifiable, the function should return an error message indicating that the input value should be a number.
"""

def cube_value(input_value):
    try:
        outcome = input_value**3
        return outcome
    except TypeError as e:
        return "Input value should be quantifiable (must be either int or float)."