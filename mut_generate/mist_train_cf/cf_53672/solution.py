"""
QUESTION:
Create a function `compute_difference(num1, num2)` that calculates and returns the difference between two numbers, including complex numbers. The function should handle non-numerical inputs by catching and returning the exception message.
"""

def compute_difference(num1, num2):
    try:
        result = num1 - num2
        return result
    except Exception as e:
        return str(e)