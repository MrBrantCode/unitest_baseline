"""
QUESTION:
Create a function named `sum_of_seven` that takes two arguments, adds 7 to their sum, and returns the result. The function should handle the case where the inputs are not numbers. The code should be written in accordance with PEP-8 guidelines.
"""

def sum_of_seven(a, b):
    try:
        return a + b + 7
    except TypeError:
        return "Error: Both a and b must be numbers (int or float)."