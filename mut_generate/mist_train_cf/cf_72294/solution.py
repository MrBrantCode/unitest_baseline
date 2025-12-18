"""
QUESTION:
Create a function named `evaluate_expression` that takes a string expression as input, evaluates the mathematical equation while following the order of operations, and returns the result. The function should handle potential cases of division by zero and complex number results, returning an error message for division by zero. The input expression may contain parentheses, arithmetic operators (+, -, *, /), and numbers.
"""

import re
import cmath

def evaluate_expression(expression):
    # Removing spaces from the expression.
    expression = expression.replace(" ", "")
    try:
        result = eval(expression)
    except ZeroDivisionError:
        return "Error: Division by zero."
    except SyntaxError:
        return "Error: Invalid syntax."
    
    # Calculate and return the result.
    return complex(result)