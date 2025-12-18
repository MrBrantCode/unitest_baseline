"""
QUESTION:
Write a function called `arithmetic_function` that takes two arguments and returns their sum. The function should handle inputs that are positive and negative integers, floating point numbers, and zero. If the inputs are not numeric, the function should return the error message "Error: Invalid input. Please provide numeric values."
"""

def arithmetic_function(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Invalid input. Please provide numeric values."