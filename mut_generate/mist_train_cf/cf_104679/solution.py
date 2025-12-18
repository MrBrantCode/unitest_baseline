"""
QUESTION:
Write a Python function called `safe_divide` that takes two parameters, `numerator` and `denominator`, and returns the result of dividing the numerator by the denominator. If the denominator is zero, the function should catch the `ZeroDivisionError` exception and return the string "Error: Division by zero is not allowed."
"""

def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."