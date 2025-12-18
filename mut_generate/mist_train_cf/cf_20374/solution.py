"""
QUESTION:
Write a function named `calculate_product` that takes two parameters `a` and `b` and returns their product. The function should attempt to convert both `a` and `b` to floating point numbers. If either `a` or `b` cannot be converted to a float, the function should return an error message "Invalid input. Please provide valid numbers." The function should adhere to the PEP8 guidelines for code style and organization.
"""

def entrance(a, b):
    try:
        a = float(a)
        b = float(b)
        return a * b
    except ValueError:
        return "Invalid input. Please provide valid numbers."